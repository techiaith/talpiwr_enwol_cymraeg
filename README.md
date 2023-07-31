[English below](#a-welsh-language-noun-chunker-for-spacy)

# Talpiwr Enwol Cymraeg ar gyfer spaCy

(Bydd angen defnyddio'r model Cymraeg canlynol: https://github.com/techiaith/parsiwr-dibyniaethau)

Dyma ymgais gychwynnol i greu fersiwn Gymraeg o dalpiwr enwol spaCy. Mae talpiau enwol yn cyfateb yn fras i'r hyn a elwir mewn Ieithyddiaeth yn ymadroddion enwol (noun phrases). Yng nghyd-destun spaCy, maen nhw’n cynrychioli rhan o’r frawddeg sy’n cynnwys enw, enw priod neu ragenw (pan fo’r rhagenw yn gweithredu lle gellid cael enw priod), yn ogystal â’r geiriau sydd, mewn dehongliad parsio dibyniaethau, yn ‘dibynnu’ ar yr enw, enw priod neu ragenw sydd dan sylw. 

Er enghraifft, yn y frawddeg isod, ystyrir *y gath fach ddu* ac *ei gwely* yn dalpiau enwol.

> Roedd **y gath fach ddu** yn cysgu ar **ei gwely**

Yn yr un modd, yn y frawddeg gyfatebol Saesneg isod, ystyrir *the little black cat* ac *her bed* yn dalpiau enwol hefyd.

> The little black cat was sleeping on her bed 

Ymdrechwyd i sicrhau cyfatebiaeth rhwng y talpiau Saesneg a gynhyrchir gan fodelau Saesneg spaCy a'r talpiau a gynhyrchir gan ein talpiwr ni wrth dalpio brawddegau cyfatebol yn y ddwy iaith (gan gydnabod nad yw hynny wastad yn briodol). Rheswm pragmataidd sydd i hynny: tueddwn i fod angen gweithredu mewn cyd-destun dwyieithog lle mae gallu cymharu yn uniongyrchol rhwng y Saesneg a’r Gymraeg yn fwy uniongyrchol yn ddefnyddiol iawn, lle bo hynny’n briodol. 

O ganlyniad, mae’r talpiwr (yn wahanol i'r egwyddorion a ddilynwyd wrth anodi’r data hyfforddi a ddefnyddiwyd i hyfforddi’r model), yn ceisio gwahaniaethu rhwng berfenwau sy’n ymddwyn yn enwol (e.e. ‘y canu da’) a berfenwau sydd yn gweithredu yn fwy berfol (e.e. ‘roeddwn yn canu’n dda’). Er mwyn cyd-fynd â disgwyliadau defnyddwyr, ac er mwyn efelychu’r dehongliad cyffredin o’r ffurfiau –ing yn y Saesneg (cymharer ‘the good singing’ ac ‘I was singing well’) sydd yn debyg i ferfenwau mewn rhai ffyrdd, dim ond y ‘canu’ enwol sy’n cael ei gydnabod i fod yn ffurfio talp enwol gennym. 

Yn ogystal â dibynnu ar egwyddorion y data a ddefnyddiwyd i hyfforddi’r model parsio dibyniaethau, mae’r talpio hefyd yn dibynnu ar gywirdeb y model hwnnw. Nid yw'r model ar hyn o bryd wastad yn parsio yn gywir. Adlewyrchiad o brinder cymharol y data hyfforddi yw hyn, nid o’i safon. Mae angen anodi rhagor o ddata er mwyn gwella’r model, a bwriadwn droi ein sylw at hynny maes o law. 

## Enghreifftiau

Rydym wedi darparu ffeil sy'n cynnwys enghreifftiau o frawddegau ag ynddynt dalpiau enwol. Yn y ffeil Python, er mwyn gwerthuso ac enghreifftio'r cod, ceisiwn ganfod y talpiau enwol a'u trosi'n dermau drwy ollwng y banodolion a'r rhagenwau o flaen pob talp. Dyma'r canlniadau:

```TERM adborth cadarnhaol
CY SENT: gellir cymell gwell perfformiad wrth ddarparu adborth cadarnhaol
EN SENT: better performance can be incentivized by providing positive feedback
CY FILTERED CHUNKS [perfformiad, adborth cadarnhaol]
EN FILTERED CHUNKS [better performance, positive feedback]
----------------
TERM asid sylffwrig
CY SENT: rhaid bod yn ofalus wrth gludo asid sylffwrig yn y labordy
EN SENT: care should be taken when transporting sulphuric acid in the laboratory
CY FILTERED CHUNKS [asid, sylffwrig, labordy]
EN FILTERED CHUNKS [care, sulphuric acid, laboratory]
----------------
TERM beicio mynydd
CY SENT: mae beicio mynydd yn gamp poblogaidd erbyn hyn
EN SENT: mountain biking is a popular sport by now
CY FILTERED CHUNKS [mynydd]
EN FILTERED CHUNKS [mountain biking, popular sport]
----------------
TERM batri alcalïaidd
CY SENT: mae lefel ph y batri alcalïaidd yn uwch na 7
EN SENT: the ph level of the alkaline battery is higher than 7
CY FILTERED CHUNKS [lefel, ph y batri alcalïaidd]
EN FILTERED CHUNKS [ph level, alkaline battery]
----------------
TERM cyfrif cadw
CY SENT: bydd hyn yn eich nadu rhag codi arian o'ch cyfrif cadw am gyfnod byr
EN SENT: this will prevent you from withdrawing cash from your deposit account for a short period
CY FILTERED CHUNKS [arian, cyfrif, cadw, gyfnod, byr]
EN FILTERED CHUNKS [cash, deposit account, short period]
----------------
TERM coetir collddail
CY SENT: rhestrwch y mathau o goed sydd i'w canfod mewn coetir collddail
EN SENT: list the types of trees that can be found in a deciduous woodland
CY FILTERED CHUNKS [mathau, goed, coetir]
EN FILTERED CHUNKS [types, trees, deciduous woodland]
----------------
TERM papur sgraffinio
CY SENT: y cam olaf yw defnyddio papur sgraffinio i lyfnhau'r pren
EN SENT: the final step is to use abrasive paper to make the wood smooth
CY FILTERED CHUNKS [papur, sgraffinio, pren]
EN FILTERED CHUNKS [final step, abrasive paper, wood]
----------------
TERM cyforgors gorlifdir
CY SENT: cafodd y cyforgors gorlifdir hwn ei ffurfio yn sgil y llifogydd difrifol diweddar
EN SENT: this floodplain raised bog was formed due to the recent severe floods
CY FILTERED CHUNKS [cyforgors, llifogydd difrifol]
EN FILTERED CHUNKS [floodplain raised bog, recent severe floods]
----------------
TERM dadansoddi ffactorau
CY SENT: dadansoddi ffactorau yw'r dull ystadegol mwyaf effeithlon
EN SENT: factor analysis is the most effective statistical method
CY FILTERED CHUNKS [dadansoddi, ffactorau, yw'r dull]
EN FILTERED CHUNKS [factor analysis, most effective statistical method]
----------------
TERM cyfnewid nwyol
CY SENT: bydd arwynebedd arwyneb mwy yn cyflymu'r cyfnewid nwyol yn yr ysgyfaint
EN SENT: a larger surface area will speed up the gaseous exchange in the lungs
CY FILTERED CHUNKS [arwynebedd, arwyneb mwy, cyfnewid nwyol, ysgyfaint]
EN FILTERED CHUNKS [larger surface area, gaseous exchange, lungs]
----------------
TERM nodyn casglu
CY SENT: seiniwch y nodyn casglu ar gychwyn yr emyn
EN SENT: sound the gathering note at the beginning of the hymn
CY FILTERED CHUNKS [seiniwch, nodyn, emyn]
EN FILTERED CHUNKS [gathering note, beginning, hymn]
----------------
TERM meddyg teulu
CY SENT: rhaid gwneud apwyntiad yn brydlon yn y bore er mwyn gweld eich meddyg teulu ar yr un diwrnod
EN SENT: an appointment must be made proptly in the morning in order to see your general practitioner on the same day
CY FILTERED CHUNKS [apwyntiad, brydlon, bore, meddyg, teulu, un diwrnod]
EN FILTERED CHUNKS [appointment, morning, order, general practitioner, same day]
----------------
TERM tymheredd egino
CY SENT: tua 18 gradd yw'r tymheredd egino delfrydol
EN SENT: 18 degrees is the ideal germination temperature
CY FILTERED CHUNKS [18 gradd, tymheredd]
EN FILTERED CHUNKS [18 degrees, ideal germination temperature]
----------------
TERM llywodraethiant byd-eang
CY SENT: fe fyddai cydweithrediad rhyngwladol yn amhosib heb gael llywodraethiant byd-eang effeithlon
EN SENT: international cooperation would be impossible without effective global governance
CY FILTERED CHUNKS [cydweithrediad rhyngwladol, llywodraethiant byd-eang]
EN FILTERED CHUNKS [international cooperation, effective global governance]
----------------
TERM llinell graen
CY SENT: mae dilyn y llinell graen yn bwysig wrth wnïo ffabrigau
EN SENT: following the grain line is important while sewing fabrics
CY FILTERED CHUNKS [llinell graen, ffabrigau]
EN FILTERED CHUNKS [grain line, sewing fabrics]
----------------
TERM bara brown garw
CY SENT: mae llai o galorïau mewn bara brown garw o gymharu â bara gwyn
EN SENT: there are less calories in granary bread than in white bread
CY FILTERED CHUNKS [llai, galorïau, brown garw, bara gwyn]
EN FILTERED CHUNKS [less calories, granary bread, white bread]
----------------
TERM tir pori
CY SENT: fe fydd yn symud y da byw i'r tir pori newydd yn y gwanwyn
EN SENT: he will be moving the live stock to new grazing land in the spring
CY FILTERED CHUNKS [byw, tir, gwanwyn]
EN FILTERED CHUNKS [live stock, new grazing land, spring]
----------------
TERM gwin coch
CY SENT: mae yfed gwin coch da gyda bwyd yn arferedig yn y wlad hon
EN SENT: drinking good red wine with food is common in this country
CY FILTERED CHUNKS [yfed, gwin coch, bwyd, wlad]
EN FILTERED CHUNKS [good red wine, food, country]
----------------
TERM graddfa gromatig harmonig
CY SENT: sylwch ar batrwm y nodau yn gweithredu fel graddfa gromatig harmonig
EN SENT: notice the note pattern acting as a harmonic chromatic scale
CY FILTERED CHUNKS [sylwch, batrwm, nodau, graddfa, gromatig, harmonig]
EN FILTERED CHUNKS [note pattern, harmonic chromatic scale]
----------------
TERM cludwr nwyddau
CY SENT: bydd rhaid cysylltu â'r cludwr nwyddau er mwyn symud y nwyddau i'r warws newydd
EN SENT: the haulage contractor must be contacted in order to move goods to the new warehouse
CY FILTERED CHUNKS [cysylltu, cludwr, nwyddau, nwyddau, warws newydd]
EN FILTERED CHUNKS [haulage contractor, order, goods, new warehouse]
----------------
TERM borio llorweddol
CY SENT: y peiriant hwn sy'n gwneud y borio llorweddol yn y graig
EN SENT: this machine performs the horizontal boring in the rockface
CY FILTERED CHUNKS [peiriant, borio llorweddol, graig]
EN FILTERED CHUNKS [machine, horizontal boring, rockface]
----------------
TERM cylchred ddŵr
CY SENT: mae cylchred ddŵr yn dychwelyd dŵr i'r tir.
EN SENT: a water cycle returns water to the land
CY FILTERED CHUNKS [cylchred, ddŵr, dŵr, tir]
EN FILTERED CHUNKS [water cycle returns water, land]
----------------
TERM chwistrell hypodermig
CY SENT: gwelodd y chwistrell hypodermig ar y llawr yn y parc
EN SENT: he saw the hypodermic needle on the floor in the park
CY FILTERED CHUNKS [chwistrell hypodermig, parc]
EN FILTERED CHUNKS [hypodermic needle, floor, park]
----------------
TERM diwydiant gweithgynhyrchu
CY SENT: prinder nwyddau yn sgil ffaeleddau'r diwydiant gweithgynhyrchu sydd yn broblem gynyddol ar gyfer masnach
EN SENT: scarcity of goods due to the shortcomings of the manufacturing industry which is an increasing problem for trade
CY FILTERED CHUNKS [prinder, nwyddau, ffaeleddau, diwydiant, gweithgynhyrchu, sydd yn broblem gynyddol, masnach]
EN FILTERED CHUNKS [scarcity, goods, shortcomings, manufacturing industry, increasing problem, trade]
----------------
TERM garddio masnachol
CY SENT: mae dealltwriaeth gyflawn o arddwriaeth yn hanfodol mewn garddio masnachol erbyn hyn
EN SENT: a complete understanding of horticulture is essential in market gardening by now
CY FILTERED CHUNKS [dealltwriaeth gyflawn, garddio masnachol]
EN FILTERED CHUNKS [complete understanding, horticulture, market gardening]
----------------
TERM pwyth padio
CY SENT: math o bwyth yw'r pwyth padio sy'n caniatáu cysylltu dau ddarn o ffabrig ynghyd
EN SENT: the padding stitch is a type of stitch which facilitates the joining of two pieces of fabric
CY FILTERED CHUNKS [math, bwyth, dau ddarn, ffabrig]
EN FILTERED CHUNKS [padding stitch, type, stitch, joining, two pieces, fabric]
----------------
TERM cytundeb paris
CY SENT: ers arwyddo cytundeb paris mae camau pellach wedi'u cymryd i frwydro newid hinsawdd
EN SENT: since the paris agreement further steps have been taken to combat climate change
CY FILTERED CHUNKS [arwyddo, cytundeb, paris, camau pellach, hinsawdd]
EN FILTERED CHUNKS [paris agreement, further steps, climate change]
----------------
TERM peintio paneli
CY SENT: mae hi'n casglu paneli pren ar gyfer ei gwaith peintio paneli
EN SENT: she is gathering wood panels for her panel painting work
CY FILTERED CHUNKS [paneli, pren, gwaith, paneli]
EN FILTERED CHUNKS [wood panels, panel painting work]
----------------
TERM gwaith cymdeithasol
CY SENT: mae hyn yn rhoi'r sgiliau i fyfyrwyr ac yn eu paratoi i gymhwyso fel gweithwyr cymdeithasol a dechrau swyddi gwaith cymdeithasol proffesiynol o fewn y gweithlu gofal cymdeithasol. 
EN SENT: this provides students with the skills to qualify as social workers and take up professional social work posts within the social care workforce.
CY FILTERED CHUNKS [sgiliau, fyfyrwyr, gymhwyso, gweithwyr cymdeithasol, dechrau, swyddi, gwaith cymdeithasol, fewn y gweithlu, gofal cymdeithasol]
EN FILTERED CHUNKS [students, skills, social workers, professional social work posts, social care workforce]
----------------
TERM cyllell balet
CY SENT: defnyddio cyllell balet i gymysgu'r paent
EN SENT: using a palette knife to mix the paint
CY FILTERED CHUNKS [defnyddio, cyllell balet, paent]
EN FILTERED CHUNKS [palette knife, paint]
----------------
```

# A Welsh-language Noun Chunker for spaCy

(Use the following model: https://github.com/techiaith/parsiwr-dibyniaethau)

This is an initial attempt to create a Welsh version of spaCy's Noun Chunk feature. Noun chunks roughly correspond to elements known as noun phrases in Linguistics. In the spaCy context, they represent a part of the sentence that contains a noun, a proper noun or a pronoun (when that pronoun appears in place of a proper noun) in addition to the words which 'depend' (according to the principles of dependency parsing) on said noun, proper noun or pronoun. 

For example, in the sentence below, *y gath fach ddu* ac *ei gwely* are considered noun chunks.

> Roedd **y gath fach ddu** yn cysgu ar **ei gwely**

Similarly, in the corresponding English sentence below, *the little black cat* and *her bed* are also considered noun chunks.

> The **little black cat** was sleeping on **her bed**

We have strived to ensure that the English language chunks produced by spaCy's English language models, and the chunks produced by our Welsh language chunker, correspond when chunking equivalent sentences in both languages (although we recognise that this is not always appropriate). There is a pragmatic reason for that: we tend to need to act in a bilingual context where being able to compare directly between English and Welsh is very useful, where appropriate. 

As a result, the chunker (unlike the principles followed when annotating the training data used to train the model), tries to distinguish between verbnouns that behave nominally (e.g. ‘y canu da’- 'the good singing') and verbnouns which function more verbally (e.g. ‘roeddwn yn canu’n dda’ - 'I was singing well'). In order to match user expectations, and to emulate the common interpretation of the –ing forms in English (compare 'the good singing' and 'I was singing well') which are similar to verbnouns in some ways, only the nominal 'canu' is recognized by us as forming a noun chunk. 

As well as depending on the principles of the data used to train the dependency parsing model, the chunking also depends on the accuracy of that model. The model currently does not always parse correctly. This reflects the relative scarcity of the training data, not its quality. More data needs to be annotated in order to improve the model, and we intend to turn our attention to that in due course. 

## Examples

We have provided a file containing examples of sentences containing noun chunks. In the Python file, in order to evaluate and exemplify the code, we try to find the noun chunks and convert them into terms by discarding the articles and pronouns at the start of each chunk. Here are the results:

```TERM adborth cadarnhaol
CY SENT: gellir cymell gwell perfformiad wrth ddarparu adborth cadarnhaol
EN SENT: better performance can be incentivized by providing positive feedback
CY FILTERED CHUNKS [perfformiad, adborth cadarnhaol]
EN FILTERED CHUNKS [better performance, positive feedback]
----------------
TERM asid sylffwrig
CY SENT: rhaid bod yn ofalus wrth gludo asid sylffwrig yn y labordy
EN SENT: care should be taken when transporting sulphuric acid in the laboratory
CY FILTERED CHUNKS [asid, sylffwrig, labordy]
EN FILTERED CHUNKS [care, sulphuric acid, laboratory]
----------------
TERM beicio mynydd
CY SENT: mae beicio mynydd yn gamp poblogaidd erbyn hyn
EN SENT: mountain biking is a popular sport by now
CY FILTERED CHUNKS [mynydd]
EN FILTERED CHUNKS [mountain biking, popular sport]
----------------
TERM batri alcalïaidd
CY SENT: mae lefel ph y batri alcalïaidd yn uwch na 7
EN SENT: the ph level of the alkaline battery is higher than 7
CY FILTERED CHUNKS [lefel, ph y batri alcalïaidd]
EN FILTERED CHUNKS [ph level, alkaline battery]
----------------
TERM cyfrif cadw
CY SENT: bydd hyn yn eich nadu rhag codi arian o'ch cyfrif cadw am gyfnod byr
EN SENT: this will prevent you from withdrawing cash from your deposit account for a short period
CY FILTERED CHUNKS [arian, cyfrif, cadw, gyfnod, byr]
EN FILTERED CHUNKS [cash, deposit account, short period]
----------------
TERM coetir collddail
CY SENT: rhestrwch y mathau o goed sydd i'w canfod mewn coetir collddail
EN SENT: list the types of trees that can be found in a deciduous woodland
CY FILTERED CHUNKS [mathau, goed, coetir]
EN FILTERED CHUNKS [types, trees, deciduous woodland]
----------------
TERM papur sgraffinio
CY SENT: y cam olaf yw defnyddio papur sgraffinio i lyfnhau'r pren
EN SENT: the final step is to use abrasive paper to make the wood smooth
CY FILTERED CHUNKS [papur, sgraffinio, pren]
EN FILTERED CHUNKS [final step, abrasive paper, wood]
----------------
TERM cyforgors gorlifdir
CY SENT: cafodd y cyforgors gorlifdir hwn ei ffurfio yn sgil y llifogydd difrifol diweddar
EN SENT: this floodplain raised bog was formed due to the recent severe floods
CY FILTERED CHUNKS [cyforgors, llifogydd difrifol]
EN FILTERED CHUNKS [floodplain raised bog, recent severe floods]
----------------
TERM dadansoddi ffactorau
CY SENT: dadansoddi ffactorau yw'r dull ystadegol mwyaf effeithlon
EN SENT: factor analysis is the most effective statistical method
CY FILTERED CHUNKS [dadansoddi, ffactorau, yw'r dull]
EN FILTERED CHUNKS [factor analysis, most effective statistical method]
----------------
TERM cyfnewid nwyol
CY SENT: bydd arwynebedd arwyneb mwy yn cyflymu'r cyfnewid nwyol yn yr ysgyfaint
EN SENT: a larger surface area will speed up the gaseous exchange in the lungs
CY FILTERED CHUNKS [arwynebedd, arwyneb mwy, cyfnewid nwyol, ysgyfaint]
EN FILTERED CHUNKS [larger surface area, gaseous exchange, lungs]
----------------
TERM nodyn casglu
CY SENT: seiniwch y nodyn casglu ar gychwyn yr emyn
EN SENT: sound the gathering note at the beginning of the hymn
CY FILTERED CHUNKS [seiniwch, nodyn, emyn]
EN FILTERED CHUNKS [gathering note, beginning, hymn]
----------------
TERM meddyg teulu
CY SENT: rhaid gwneud apwyntiad yn brydlon yn y bore er mwyn gweld eich meddyg teulu ar yr un diwrnod
EN SENT: an appointment must be made proptly in the morning in order to see your general practitioner on the same day
CY FILTERED CHUNKS [apwyntiad, brydlon, bore, meddyg, teulu, un diwrnod]
EN FILTERED CHUNKS [appointment, morning, order, general practitioner, same day]
----------------
TERM tymheredd egino
CY SENT: tua 18 gradd yw'r tymheredd egino delfrydol
EN SENT: 18 degrees is the ideal germination temperature
CY FILTERED CHUNKS [18 gradd, tymheredd]
EN FILTERED CHUNKS [18 degrees, ideal germination temperature]
----------------
TERM llywodraethiant byd-eang
CY SENT: fe fyddai cydweithrediad rhyngwladol yn amhosib heb gael llywodraethiant byd-eang effeithlon
EN SENT: international cooperation would be impossible without effective global governance
CY FILTERED CHUNKS [cydweithrediad rhyngwladol, llywodraethiant byd-eang]
EN FILTERED CHUNKS [international cooperation, effective global governance]
----------------
TERM llinell graen
CY SENT: mae dilyn y llinell graen yn bwysig wrth wnïo ffabrigau
EN SENT: following the grain line is important while sewing fabrics
CY FILTERED CHUNKS [llinell graen, ffabrigau]
EN FILTERED CHUNKS [grain line, sewing fabrics]
----------------
TERM bara brown garw
CY SENT: mae llai o galorïau mewn bara brown garw o gymharu â bara gwyn
EN SENT: there are less calories in granary bread than in white bread
CY FILTERED CHUNKS [llai, galorïau, brown garw, bara gwyn]
EN FILTERED CHUNKS [less calories, granary bread, white bread]
----------------
TERM tir pori
CY SENT: fe fydd yn symud y da byw i'r tir pori newydd yn y gwanwyn
EN SENT: he will be moving the live stock to new grazing land in the spring
CY FILTERED CHUNKS [byw, tir, gwanwyn]
EN FILTERED CHUNKS [live stock, new grazing land, spring]
----------------
TERM gwin coch
CY SENT: mae yfed gwin coch da gyda bwyd yn arferedig yn y wlad hon
EN SENT: drinking good red wine with food is common in this country
CY FILTERED CHUNKS [yfed, gwin coch, bwyd, wlad]
EN FILTERED CHUNKS [good red wine, food, country]
----------------
TERM graddfa gromatig harmonig
CY SENT: sylwch ar batrwm y nodau yn gweithredu fel graddfa gromatig harmonig
EN SENT: notice the note pattern acting as a harmonic chromatic scale
CY FILTERED CHUNKS [sylwch, batrwm, nodau, graddfa, gromatig, harmonig]
EN FILTERED CHUNKS [note pattern, harmonic chromatic scale]
----------------
TERM cludwr nwyddau
CY SENT: bydd rhaid cysylltu â'r cludwr nwyddau er mwyn symud y nwyddau i'r warws newydd
EN SENT: the haulage contractor must be contacted in order to move goods to the new warehouse
CY FILTERED CHUNKS [cysylltu, cludwr, nwyddau, nwyddau, warws newydd]
EN FILTERED CHUNKS [haulage contractor, order, goods, new warehouse]
----------------
TERM borio llorweddol
CY SENT: y peiriant hwn sy'n gwneud y borio llorweddol yn y graig
EN SENT: this machine performs the horizontal boring in the rockface
CY FILTERED CHUNKS [peiriant, borio llorweddol, graig]
EN FILTERED CHUNKS [machine, horizontal boring, rockface]
----------------
TERM cylchred ddŵr
CY SENT: mae cylchred ddŵr yn dychwelyd dŵr i'r tir.
EN SENT: a water cycle returns water to the land
CY FILTERED CHUNKS [cylchred, ddŵr, dŵr, tir]
EN FILTERED CHUNKS [water cycle returns water, land]
----------------
TERM chwistrell hypodermig
CY SENT: gwelodd y chwistrell hypodermig ar y llawr yn y parc
EN SENT: he saw the hypodermic needle on the floor in the park
CY FILTERED CHUNKS [chwistrell hypodermig, parc]
EN FILTERED CHUNKS [hypodermic needle, floor, park]
----------------
TERM diwydiant gweithgynhyrchu
CY SENT: prinder nwyddau yn sgil ffaeleddau'r diwydiant gweithgynhyrchu sydd yn broblem gynyddol ar gyfer masnach
EN SENT: scarcity of goods due to the shortcomings of the manufacturing industry which is an increasing problem for trade
CY FILTERED CHUNKS [prinder, nwyddau, ffaeleddau, diwydiant, gweithgynhyrchu, sydd yn broblem gynyddol, masnach]
EN FILTERED CHUNKS [scarcity, goods, shortcomings, manufacturing industry, increasing problem, trade]
----------------
TERM garddio masnachol
CY SENT: mae dealltwriaeth gyflawn o arddwriaeth yn hanfodol mewn garddio masnachol erbyn hyn
EN SENT: a complete understanding of horticulture is essential in market gardening by now
CY FILTERED CHUNKS [dealltwriaeth gyflawn, garddio masnachol]
EN FILTERED CHUNKS [complete understanding, horticulture, market gardening]
----------------
TERM pwyth padio
CY SENT: math o bwyth yw'r pwyth padio sy'n caniatáu cysylltu dau ddarn o ffabrig ynghyd
EN SENT: the padding stitch is a type of stitch which facilitates the joining of two pieces of fabric
CY FILTERED CHUNKS [math, bwyth, dau ddarn, ffabrig]
EN FILTERED CHUNKS [padding stitch, type, stitch, joining, two pieces, fabric]
----------------
TERM cytundeb paris
CY SENT: ers arwyddo cytundeb paris mae camau pellach wedi'u cymryd i frwydro newid hinsawdd
EN SENT: since the paris agreement further steps have been taken to combat climate change
CY FILTERED CHUNKS [arwyddo, cytundeb, paris, camau pellach, hinsawdd]
EN FILTERED CHUNKS [paris agreement, further steps, climate change]
----------------
TERM peintio paneli
CY SENT: mae hi'n casglu paneli pren ar gyfer ei gwaith peintio paneli
EN SENT: she is gathering wood panels for her panel painting work
CY FILTERED CHUNKS [paneli, pren, gwaith, paneli]
EN FILTERED CHUNKS [wood panels, panel painting work]
----------------
TERM gwaith cymdeithasol
CY SENT: mae hyn yn rhoi'r sgiliau i fyfyrwyr ac yn eu paratoi i gymhwyso fel gweithwyr cymdeithasol a dechrau swyddi gwaith cymdeithasol proffesiynol o fewn y gweithlu gofal cymdeithasol. 
EN SENT: this provides students with the skills to qualify as social workers and take up professional social work posts within the social care workforce.
CY FILTERED CHUNKS [sgiliau, fyfyrwyr, gymhwyso, gweithwyr cymdeithasol, dechrau, swyddi, gwaith cymdeithasol, fewn y gweithlu, gofal cymdeithasol]
EN FILTERED CHUNKS [students, skills, social workers, professional social work posts, social care workforce]
----------------
TERM cyllell balet
CY SENT: defnyddio cyllell balet i gymysgu'r paent
EN SENT: using a palette knife to mix the paint
CY FILTERED CHUNKS [defnyddio, cyllell balet, paent]
EN FILTERED CHUNKS [palette knife, paint]
----------------
```
