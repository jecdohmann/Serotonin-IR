#!/usr/bin/python
# -*- coding: utf-8 -*-
strs=[ur"\b2c ?b",
ur"\b2c ?e",
ur"\b2c ?t ?2",
ur"\b4c ?t ?2",
ur"\b5 ?ct",
ur"\b5 ?mt",
ur"\b5 ?meo ?dipt",
ur"\b5 ?meo ?dmt",
ur"\b5 ?meo ?mipt",
ur"\b5 ?meo ?tmt",
ur"\b6 ?f ?dmt",
ur"\badatanserin",
ur"\baet",
ur"\bamphetamine",
ur"\bamt",
ur"\baripiprazole",
ur"\basenapine",
ur"\bbacoside",
ur"\bbay r 1531",
ur"\bbefiradol",
ur"\bbinospirone",
ur"\bbrexpiprazole",
ur"\bbufotenin",
ur"\bbuspirone",
ur"\bcannabidiol",
ur"\bcariprazine",
ur"\bclozapine",
ur"\bcis ?2a",
ur"\bdihydroergotamine",
ur"\bdimethyltryptamine",
ur"\bdipt",
ur"\bdoet",
ur"\bdoi",
ur"\bdpt",
ur"\bebalzotan",
ur"\beltoprazine",
ur"\bemdt",
ur"\bergotamine",
ur"\betoperidone",
ur"\bf ?11461",
ur"\bf ?12826",
ur"\bf ?13714",
ur"\bf ?14679",
ur"\bflesinoxan",
ur"\bflibanserin",
ur"\bginkgo biloba",
ur"\bgepirone",
ur"\bhaloperidol",
ur"\blamotrigine",
ur"\bipsapirone",
ur"\blimonene",
ur"\blisuride",
ur"\blurasidone",
ur"\bly ?301317",
ur"\blysergic acid diethylamide",
ur"\blsd",
ur"\bmescaline",
ur"\b34 ?methylenedioxyamphetamine",
ur"\bmethylphenidate",
ur"\bmethysergide",
ur"\bnaluzotan",
ur"\bnbump",
ur"\bnefazodone",
ur"\bolanzapine",
ur"\bosemozotan",
ur"\bperospirone",
ur"\bpyrimidinylpiperazine",
ur"\bpiclozotan",
ur"\bpsilocin",
ur"\bpsilocybin",
ur"\bquetiapine",
ur"\brauwolscine",
ur"\brr ?2b",
ur"\bru ?24969",
ur"\bs ?15535",
ur"\bsarizotan",
ur"\bss ?2c",
ur"\bssr ?181507",
ur"\bsunepitron",
ur"\btandospirone",
ur"\btiospirone",
ur"\btrazodone",
ur"\btrifluoromethylphenylpiperazine",
ur"\btrimethoxyamphetamine",
ur"\bumespirone",
ur"\burapidil",
ur"\bvilazodone",
ur"\bxaliproden",
ur"\byohimbine",
ur"\bzalospirone",
ur"\bziprasidone",
ur"\b8 ?oh ?dpat",
ur"\balnespirone",
ur"\beptapirone",
ur"\bf ?15599",
ur"\blesopitron",
ur"\bmkc ?242",
ur"\bly ?293284",
ur"\brepinotan",
ur"\bu ?92016 ?a",
ur"\bvortioxetine",
ur"\boxymetazoline",
ur"\bsumatriptan",
ur"\bzolmitriptan",
ur"\b5 ?carboxamidotryptamine",
ur"\bcgs ?12066a",
ur"\bcp ?93129",
ur"\bcp ?94253",
ur"\bcp ?122288",
ur"\bcp ?135807",
ur"\bdextromethorphan",
ur"\b5 ?nonyloxytryptamine",
ur"\b5 ?t ?butyl ?n ?methyltryptamine",
ur"\bcp ?286601",
ur"\bpnu ?109291",
ur"\bs ?34 ?dihydro ?1 ?2 ?4 ?4 ?methoxyphenyl ?1 ?piperazinylethyl ?n ?methyl ?1h ?2 ?benzopyran ?6 ?carboxamide",
ur"\bpnu ?142633",
ur"\b1s ?1 ?2 ?4 ?4 ?aminocarbonylphenyl ?1 ?piperazinylethyl ?34 ?dihydro ?n ?methyl ?1h ?2 ?benzopyran ?6 ?carboxamide",
ur"\bgr ?46611",
ur"\b3 ?3 ?2 ?dimethylaminoethyl ?1h ?indol ?5 ?yl ?n ?4 ?methoxybenzylacrylamide",
ur"\bl ?694247",
ur"\b2 ?5 ?3 ?4 ?methylsulfonylaminobenzyl ?124 ?oxadiazol ?5 ?yl ?1h ?indol ?3 ?ylethanamine",
ur"\bl ?772405",
ur"\bbrl ?54443",
ur"\b5 ?hydroxy ?3 ?1 ?methylpiperidin ?4 ?yl ?1h ?indole  ? mixed 5 ?ht1e1fagonist",
ur"\bly334370",
ur"\bly344864",
ur"\bagmatine",
ur"\b25i ?nboh",
ur"\b25i ?nbome",
ur"\bfecimbi ?36",
ur"\btcb ?2",
ur"\bmexamine",
ur"\bo ?4310",
ur"\bpha ?57378",
ur"\b25b ?nbome",
ur"\bcimbi ?36",
ur"\b25c ?nbome",
ur"\b25cn ?nboh",
ur"\bbromo ?dragonfly",
ur"\br ?doi",
ur"\befavirenz",
ur"\bjuncosamine",
ur"\bmefloquine",
ur"\bsn ?22",
ur"\bbw ?723c86",
ur"\bro60 ?0175",
ur"\bver ?3323",
ur"\ba ?methyl ?5 ?ht",
ur"\b6 ?apb",
ur"\bly ?266097",
ur"\bguanfacine",
ur"\bmdma",
ur"\bmda",
ur"\bmem",
ur"\bpergolide",
ur"\bcabergoline",
ur"\bnorfenfluramine",
ur"\bchlorphentermine",
ur"\baminorex",
ur"\bmcpp",
ur"\bbromo ?dragonfly",
ur"\bdmt",
ur"\bpsilocin",
ur"\ba ?372159",
ur"\bal ?38022a",
ur"\bcp ?809101",
ur"\bcpd ?1",
ur"\bfenfluramine",
ur"\blorcaserin",
ur"\bmesulergine",
ur"\bmk ?212",
ur"\bnaphthylisopropylamine",
ur"\borg 12962",
ur"\borg ?37684",
ur"\boxaflozane",
ur"\bpnu ?22394",
ur"\bpnu ?181731",
ur"\blysergamides",
ur"\bphenethylamines",
ur"\bdom",
ur"\bpiperazines",
ur"\btfmpp",
ur"\bvabicaserin",
ur"\bway ?629",
ur"\bway ?161503",
ur"\bway ?163909",
ur"\bym ?348",
ur"\bcereulide",
ur"\b2 ?methyl ?5 ?ht",
ur"\balpha ?methyltryptamine",
ur"\bchlorophenylbiguanide",
ur"\bethanol",
ur"\bibogaine",
ur"\bphenylbiguanide",
ur"\bquipazine",
ur"\brs ?56812",
ur"\bsr ?57227",
ur"\bvarenicline",
ur"\bym ?31636",
ur"\bbimu ?8",
ur"\bcisapride",
ur"\bcj ?033466",
ur"\bml ?10302",
ur"\bmosapride",
ur"\bprucalopride",
ur"\brenzapride",
ur"\brs ?67506",
ur"\brs ?67333",
ur"\bsl650155",
ur"\btegaserod",
ur"\bzacopride",
ur"\bmetoclopramide",
ur"\bsulpiride",
ur"\blsd ?lysergic acid",
ur"\bvalerenic acid",
ur"\b2 ?ethyl ?5 ?methoxy ?nn ?dimethyltryptamine",
ur"\bway ?181187",
ur"\bway ?208466",
ur"\bn ?inden ?5 ?ylimidazothiazole ?5 ?sulfonamide 43",
ur"\be ?6837",
ur"\be ?6801",
ur"\bemd ?386088",
ur"\b5 ?methoxytryptamine",
ur"\b5 ?meot",
ur"\bas ?19",
ur"\be ?55888",
ur"\be ?57431",
ur"\blp ?12",
ur"\b4 ?2 ?diphenyl ?n ?1234 ?tetrahydronaphthalen ?1 ?yl ?1 ?piperazinehexanamide",
ur"\blp ?44",
ur"\b4 ?2 ?methylthiophenyl ?n ?1234 ?tetrahydro ?1 ?naphthalenyl ?1 ?piperazinehexanamide",
ur"\blp ?211",
ur"\bmsd ?5a",
ur"\bn ?methylserotonin",
ur"\bn ?1234 ?tetrahydronaphthalen ?1 ?yl ?4 ?aryl ?1 ?piperazinehexanamides",
ur"\bnn ?dimethyltryptamine",
ur"\bra ?71 ?2 ?diphenylpiperazine",
ur"\bagh ?107",
ur"\bah ?494",
ur"\b3 ?1 ?ethyl ?1h ?imidazol ?5 ?yl ?1h ?indole ?5 ?carboxamide",
ur"\bagh ?192"]