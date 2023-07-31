# TO BE ADDED AS spacy/lang/cy/syntax_iterators.py WHEN TESTING COMPLETE
import spacy

from typing import Union, Iterator, Tuple
from spacy.symbols import NOUN, PROPN, PRON
from spacy.errors import Errors
from spacy.tokens import Doc, Span

def welsh_noun_chunks(doclike: Union[Doc, Span]) -> Iterator[Tuple[int, int, int]]:
    """
    Detect base noun phrases from a dependency parse. Works on both Doc and Span.
    """
    labels = [
        "nsubj",
        "nsubj:pass",
        "obj",
        "obl",
        "obl:agent",
        "obl:arg",
        "obl:mod",
        "nmod",
        "pcomp",
        "appos",
        "ROOT",
    ]
    post_modifiers = ["flat", "flat:name", "flat:foreign", "fixed", "compound"]
    doc = doclike.doc  # Ensure works on both Doc and Span.
    if not doc.has_annotation("DEP"):
        raise ValueError(Errors.E029)
    np_deps = {doc.vocab.strings.add(label) for label in labels}
    np_modifs = {doc.vocab.strings.add(modifier) for modifier in post_modifiers}
    np_label = doc.vocab.strings.add("NP")
    adj_label = doc.vocab.strings.add("amod")
    det_label = doc.vocab.strings.add("det")
    det_pos = doc.vocab.strings.add("DET")
    adp_pos = doc.vocab.strings.add("ADP")
    conj_label = doc.vocab.strings.add("conj")
    conj_pos = doc.vocab.strings.add("CCONJ")
    prev_end = -1
    for i, word in enumerate(doclike):
        if word.pos not in (NOUN, PROPN, PRON):
            continue

        # Prevent verbal verbouns  from forming chunks
        # Verbnouns with children with ADJ or DET are nominal verbnouns, not verbal verbnouns
        if "ADJ" not in [t.pos_ for t in word.children] and "DET" not in [t.pos_ for t in word.children]:

            # Exclude verbnouns with prepositions as auxiliaries: "yn canu", "wedi canu" etc.
            # Not foolproof - should really also check for aux verb - "roedd" .. yn canu etc.

            if i > 1: # # AUX can be AUX verbs too so need to check form is yn/wedi/newydd etc.
                if word.tag_ == "verbnoun" and doclike[word.i - 1].pos_ in ["AUX"] \
                and doclike[word.i - 1].text in ["yn", "wedi", "newydd"]:
                    #print ("AUX + VN:", word)
                    continue
            if i > 1: # wrth ddychwel(?), dan ganu, heb falio, ar  etc.
                # Will create some rare false positives
                if word.tag_ == "verbnoun" and doclike[word.i - 1].pos_ in ["ADP"]:
                    #print ("ADP + VN:", word)
                    continue
            if i > 2: # yn ei gario etc.
                if word.tag_ == "verbnoun" and doclike[word.i - 2].pos_ in ["AUX", "ADP"] \
                and doclike[word.i - 2].text in ["yn", "wedi", "newydd"] \
                and doclike[word.i - 1].pos_ == "PRON":
                    #print ("AUX/ADP + PRON + VN:", word)
                    continue 

        # Filter out compound prepositions
        if i > 1:
            if doclike[word.i - 1].text == "er" and word.text == "mwyn":
                continue
            if doclike[word.i - 1].text == "ar" and word.text == "gyfer":
                continue

        # Prevent nested chunks from being produced
        if word.left_edge.i <= prev_end:
            continue
        if word.dep in np_deps:
            right_childs = list(word.rights)
            right_child = right_childs[0] if right_childs else None

            if right_child:
                if (
                    right_child.dep == adj_label
                ):  # allow chain of adjectives by expanding to right
                    right_end = right_child.right_edge
                elif (
                    right_child.dep == det_label and right_child.pos == det_pos
                ):  # cut relative pronouns here
                    right_end = right_child
                elif right_child.dep in np_modifs:  # Check if we can expand to right
                    right_end = word.right_edge
                else:
                    right_end = word
            else:
                right_end = word
            prev_end = right_end.i

            left_index = word.left_edge.i
            left_index = left_index + 1 if word.left_edge.pos == adp_pos else left_index

            yield left_index, right_end.i + 1, np_label
        elif word.dep == conj_label:
            head = word.head
            while head.dep == conj_label and head.head.i < head.i:
                head = head.head
            # If the head is an NP, and we're coordinated to it, we're an NP
            if head.dep in np_deps:
                prev_end = word.i

                left_index = word.left_edge.i  # eliminate left attached conjunction
                left_index = (
                    left_index + 1 if word.left_edge.pos == conj_pos else left_index
                )
                yield left_index, word.i + 1, np_label


def wnc_output2nc(nc_tuple, doc):
    return (doc[nc_tuple[0]:nc_tuple[1]])

# USE THE FOLLOWING WELSH MODEL: https://github.com/techiaith/parsiwr-dibyniaethau
nlp_cy = spacy.load("cy_ud_cy_ccg")
nlp_en = spacy.load("en_core_web_lg")

# LOAD EXAMPLES
with open("cy_term_example_sents.txt") as f:
    lines = f.readlines()

# CONVERT EXAMPLES TO A DICTIONARY
entries = []
for line in lines:
    if line:
        entry = {}
        print (line)
        entry["id"], entry["pos"], entry["term"], entry["sent"], entry["sent_en"] = line.replace("’", "'").strip().lower().split("\t")
        entry["term"] = entry["term"].strip()
        entry["doc_en"] = nlp_en(entry["sent_en"])
        entry["doc_cy"] = nlp_cy(entry["sent"])
        entries.append(entry)


# ADD CHUNKS WHERE DETs AND PRONS HAVE BEEN FILTERED OUT 
filtered_chunks_en = []
filtered_chunks_cy = []
for entry in entries:
    doc_en = nlp_en(entry["sent_en"])
    doc_cy = nlp_cy(entry["sent"])
    entry["ncs_en"] = []
    entry["ncs_cy"] = []
    entry["filtered_ncs_en"] = []
    entry["filtered_ncs_cy"] = []
    entry["new_ncs_cy"] = []
    entry["filtered_new_ncs_cy"] = []
    for nc_en in doc_en.noun_chunks:
        print (nc_en)
        entry["ncs_en"].append(nc_en)
        if nc_en[0].pos_ in ["DET", "PRON"]:
            if nc_en[1:]:
                filtered_chunks_en.append(nc_en[1:])
                entry["filtered_ncs_en"].append(nc_en[1:])
        else:
            filtered_chunks_en.append(nc_en)
            entry["filtered_ncs_en"].append(nc_en)
    
    for nc_cy in doc_cy.noun_chunks:
        if nc_cy[0].pos_ in ["DET", "PRON"] or nc_cy[0].text in ["rhaid", "angen"]:
            if nc_cy[1:]:
                filtered_chunks_cy.append(nc_cy[1:])
                entry["filtered_ncs_cy"].append(nc_cy[1:])
        else:
            filtered_chunks_cy.append(nc_cy)
            entry["filtered_ncs_cy"].append(nc_cy)

    for nc_cy_np in welsh_noun_chunks(doc_cy):
        nc_cy = wnc_output2nc(nc_cy_np, doc_cy)
        if nc_cy[0].pos_ in ["DET", "PRON"] or nc_cy[0].text in ["rhaid", "angen", "sgil"]:
            if nc_cy[1:]:
                entry["filtered_new_ncs_cy"].append(nc_cy[1:])
        else:
            entry["filtered_new_ncs_cy"].append(nc_cy)


# PRINT SENTS AND FILTERED CHUNKS in EN AND CY FOR COMPARISON
for i, entry in enumerate(entries):
    print ("TERM", entry["term"])
    print ("CY SENT:", entry["sent"])
    print ("EN SENT:", entry["sent_en"])
    # print ("DEFAULT CY", entry["filtered_ncs_cy"])
    print ("CY FILTERED CHUNKS", entry["filtered_new_ncs_cy"])
    print ("EN FILTERED CHUNKS", entry["filtered_ncs_en"])
    print ("----------------")