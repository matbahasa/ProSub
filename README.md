# ProSub

## Introduction
This repository contains resources developed by the JSPS KAKENHI project "A cross-linguistic study of pronoun substitutes and address terms" ([JP20H01255](https://kaken.nii.ac.jp/ja/grant/KAKENHI-PROJECT-20H01255/)).

## How to cite
- (Common questionnaire)  
  岡野賢二, 野元裕樹, スニサーウィッタヤーパンヤーノン, トゥザライン, 春日淳. 2022.[「アジア三言語における代名詞代用・呼びかけ語の共通項目調査」](https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/D1-2.pdf)『言語処理学会第28回年次大会発表論文集』, 69-73.
- (Dataset)  
  谷口龍子, 大久保弥, 野元裕樹, 南潤珍. 2022. [「代名詞代用・呼びかけ表現の多言語データセット」](https://www.ls-japan.org/modules/documents/LSJpapers/meeting/164/handouts/p/P-6_164.pdf).『日本言語学会第164回大会予稿集』, 307-313.
- (Corpus annotations)  
  Nomoto, Hiroki, Ryuko Taniguchi, Shiori Nakamura, Yunjin Nam, Sri Budi Lestari, Sunisa Wittayapanyanon (Saito), Virach Sornlertlamvanich, Atsushi Kasuga, Kenji Okano and Thuzar Hlaing. 2023. [Pronoun substitute annotation in seven Asian languages](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P9-4.pdf). _Proceedings of the Twenty-Ninth Annual Meeting of the Association for Natural Language Processing_, 2242-2247.
- (Speech function annotation in Japanese)  
  中村栞, 梅田里菜, 谷口龍子. 2024.「発話機能の種類と自称詞・対称詞の明示化」東京外国語大学国際日本研究センター対照日本語学部門主催『外国語と日本語との対照言語学的研究』第40回研究会における発表論文.

```bib
@InProceedings{OkanoEtAl22,
    author = {Okano, Kenji and Nomoto, Hiroki and Wittayapanyanon, Sunisa and Thuzar Hlaing and Kasuga, Atsushi},
    year = {2022},
    title = {Ajia sangengo niokeru daimeishidaiyou, yobikakego no kyoutsuukoumoku chousa},
    booktitle = {Proceedings of the Twenty-Eighth Annual Meeting of the {A}ssociation for {N}atural {L}anguage {P}rocessing},
    pages = {69-73},
    url = {https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/D1-2.pdf},
    note = {An investigation of pronoun substitutes and address terms in three Asian languages based on a common questionnaire}
}

@InProceedings{TaniguchiEtAl22,
    author = {Taniguchi, Ryuko and Okubo, Wataru and Nomoto, Hiroki and Nam, Yunjin},
    year = {2022},
    title = {Daimeishidaiyou, yobikake hyougen no tagengo deetasetto},
    booktitle = {The Proceedings of the 164th Meeting of the {L}inguistic {S}ociety of {J}apan},
    pages = {307-313},
    url = {https://www.ls-japan.org/modules/documents/LSJpapers/meeting/164/handouts/p/P-6_164.pdf},
    note = {A multilingual dataset of pronoun substitutes and address terms}
}

@InProceedings{NomotoEtAl23,
    author = {Nomoto, Hiroki and Taniguchi, Ryuko and Nakamura, Shiori and Nam, Yunjin and Lestari, Sri Budi and Wittayapanyanon (Saito), Sunisa and Sornlertlamvanich, Virach and Kasuga, Atsushi and Okano, Kenji and Thuzar Hlaing},
    year = {2023},
    title = {Pronoun substitute annotation in seven {A}sian languages},
    booktitle = {Proceedings of the Twenty-Ninth Annual Meeting of the {A}ssociation for {N}atural {L}anguage {P}rocessing},
    pages = {2242-2247},
    url = {https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P9-4.pdf}
}

@misc{NakamuraEtAl24,
    author = {Nakamura, Shiori and Umeda, Rina and Taniguchi, Ryuko},
    year = {2024},
    title = {Hatsuwakinoo no shurui to jishooshi, taishooshi no meijika},
    howpublished = {Paper presented at the 40th research seminar on "Contrastive Studies of Japanese and Other Languages", Contrastive Japanese Division, International Center for Japanese Studies, Tokyo University of Foreign Studies},
    note = {Speech function types and the explict realization of speaker- and addressee-referring expressions}
}
```

## Contents
- `common_questionnaire.tsv` A common questionnaire for investigating pronoun substitutes and address terms
- `data_all_v1.0.tsv` Initial data based on the common questionnaire in Japanese, Korean, Indonesian, Malay, Javanese, Thai, Vietnamese and Thai in the tag-separated format.  English translations are not complete.  Ensure that the encoding is set as UTF-8 when you open the file with MS Excel.
- `data_all_v1.0.json` Initial data based on the common questionnaire in Japanese, Korean, Indonesian, Malay, Javanese, Thai, Vietnamese and Thai in the json format.  English translations are not complete.
- `data_all_v2.0.tsv` Revised data based on the common questionnaire in Japanese, Korean, Indonesian, Malay, Javanese, Thai, Vietnamese and Thai in the tag-separated format.  Ensure that the encoding is set as UTF-8 when you open the file with MS Excel.
- `data_all_v2.0.json` Revised data based on the common questionnaire in Japanese, Korean, Indonesian, Malay, Javanese, Thai, Vietnamese and Thai in the json format.
- `full_data.json` Full data collected by the project, which includes not only the data based on the common questionnaire but also the data from other sources.

## Format
### common_questionnaire.tsv
`ID [TAB] concept (Japanese) [TAB] concept (English) [TAB] WordNet synset ID [TAB] semantic category`

The semantic categories are based on the [feature system](https://github.com/matbahasa/TALPCo/blob/master/features.pdf) proposed by:  
Nomoto, Hiroki, Kenji Okano, Sunisa Wittayapanyanon and Junta Nomura. 2019. [Interpersonal meaning annotation for Asian language corpora: The case of TUFS Asian Language Parallel Corpus (TALPCo)](https://www.anlp.jp/proceedings/annual_meeting/2019/pdf_dir/D4-4.pdf).  _Proceedings of the Twenty-Fifth Annual Meeting of the Association for Natural Language Processing_, 846-849.

### data_all_v1.0.tsv, data_all_v2.0.tsv
`language code [TAB] concept ID [TAB] concept (Japanese) [TAB] concept (English) [TAB] semantic category [TAB] expression [TAB] Japanese translation of expression [TAB] English translation of expression [TAB] function [TAB] judgement [TAB] example [TAB] Japanese translation of example [TAB] English translation of example [TAB] source [TAB] notes`

### data_all_v1.0.json, data_all_v2.0.json
```json
{
     "language code": {
        "concept ID": {
            "concept_jpn": "concept (Japanese)",
            "concept_eng": "concept (English)",
            "category": "semantic category",
            "expression": [
                {
                    "form": "expression",
                    "trans_jpn": "Japanese translation of expression",
                    "trans_eng": "English translation of expression",
                    "function": {
                        "1st": {
                            "judgement": "judgement",
                            "example": [
                                {
                                    "form": "example",
                                    "trans_jpn": "Japanese translation of example",
                                    "trans_eng": "English translation of example",
                                    "source": "source",
                                    "notes": "notes"
                                }
                            ]
                        },
                        "2nd": {
                            "judgement": "judgement",
                            "example": [
                                {
                                    "form": "example",
                                    "trans_jpn": "Japanese translation of example",
                                    "trans_eng": "English translation of example",
                                    "source": "source",
                                    "notes": "notes"
                                }
                            ]
                        },
                        "address": {
                            "judgement": "judgement",
                            "example": [
                                {
                                    "form": "example",
                                    "trans_jpn": "Japanese translation of example",
                                    "trans_eng": "English translation of example",
                                    "source": "source",
                                    "notes": "notes"
                                }
                            ]
                        },
                        "title": {
                            "judgement": "judgement",
                            "example": [
                                {
                                    "form": "example",
                                    "trans_jpn": "Japanese translation of example",
                                    "trans_eng": "English translation of example",
                                    "source": "source",
                                    "notes": "notes"
                                }
                            ]
                        }
                    }
                }
            ]
        }
}
```
### full_data.json
```json
{
    "id": "ID",
    "language": "language code",
    "form": "form",
    "romanization": "romanization of the form",
    "trans_jpn": "Japanese translation of the form",
    "trans_eng": "English translation of the form",
    "wordnet_id": "wordnet synset ID",
    "wordnet_note": "notes on the wordnet information",
    "component_elements": "component elements of the form",
    "related_word": "word related to the form",
    "related_word_relation": "relation of the related word to the form",
    "1st": [
        {
            "example": "example of the 1st person function use",
            "trans_jpn": "Japanese translation of the example",
            "trans_eng": "English translation of the example",
            "source": "source of the example",
            "notes": "notes on the example"
        }
    ],
    "2nd": [
        {
            "example": "example of the 2nd person function use",
            "trans_jpn": "Japanese translation of the example",
            "trans_eng": "English translation of the example",
            "source": "source of the example",
            "notes": "notes on the example"
        }
    ],
    "address": [
        {
            "example": "example of the address term function use",
            "trans_jpn": "Japanese translation of the example",
            "trans_eng": "English translation of the example",
            "source": "source of the example",
            "notes": "notes on the example"
        }
    ],
    "title": [
        {
            "example": "example of the honorific title function use",
            "trans_jpn": "Japanese translation of the example",
            "trans_eng": "English translation of the example",
            "source": "source of the example",
            "notes": "notes on the example"
        }
    ],
    "loan_word": "whether or not the form is a loan word (true/false/null)",
    "formal_features": {
        "common_noun": "whether or not the form is a common noun (true/false/null)",
        "proper_noun_real_name": "whether or not the form is a proper name that is a real name (true/false/null)",
        "proper_noun_alias": "whether or not the form is a proper name that is an alias (true/false/null)",
        "demontrative": "whether or not the form is a proper name that is an alias (true/false/null)",
        "locative_pronoun": "whether or not the form is a proper name that is an alias (true/false/null)",
        "numeral": "whether or not the form is a numeral (true/false/null)",
        "classifier": "whether or not the form is a numeral classifier (true/false/null)",
        "quantifier": "whether or not the form is a quantifier (true/false/null)",
        "anaphor": "whether or not the form is an anaphor (i.e. reflexive or reciprocal)",
        "personal_pronoun": "whether or not the form is a personal pronoun (true/false/null)",
        "bound_morpheme": "whether or not the form is a bound morpheme (true/false/null)",
        "endearment": "whether or not the form is an expression conveying endearment (true/false/null)",
        "other": "whether or not the form belongs to none of the categories above (true/false/null)",
        "notes": "notes on the formal features of the form"
    },
    "meaning": {
        "gender": "gender",
        "marital_status": "marital status",
        "honour": "presence and kind of honour",
        "age": "age",
        "social_status": "social status",
        "role": "role",
        "group": "group",
        "formality": "formality",
        "intimacy": "intimacy",
        "number": "number"
    },
    "meaning_note": "notes on the meaning features",
    "speaker": "restriction on who uses the form",
    "memo": "notes for the item as a whole",
    "creator": "creator of the item",
    "createdAt": "date and time of item creation",
    "editor": "editor of the item",
    "updatedAt": "date and time of the last update"
}
```

The values of the meaning features are as in the table below.  The absence of a feature means that the relevant feature is unspecified (or the creator did not provide the information).

| Feature | Values |
|---------|--------|
|Gender |male, female|
|Marital\_status | married, unmarried|
|Honour |hon, anti-hon|
|Age |elder, elder.grandparent, elder.parents\_elder\_sibling, elder.parent, elder.parents\_younger\_sibling, elder.sibling, younger, younger.sibling, younger.child, mature, mature.old, mature.middle, youth|
|Social\_status |higher, equal\_or\_higher, equal, equal\_or\_lower, lower]
Role | teacher, teacher.school, teacher.university, teacher.nonK12, teacher.other, student, student.school, student.university, student.nonK12, student.other, grandparent, grandparent.paternal, grandparent.maternal, parent, child, sibling, parents\_sibling, parents\_sibling.paternal, parents\_sibling.maternal, spouse, titled, titled.head, titled.head.territory, titled.head.territory.central, titled.head.territory.local, titled.head.organization, titled.head.organization.ministry, titled.head.organization.ministry, titled.head.organization.company, titled.head.organization.education, titled.head.organization.other, titled.conferred, titled.other, non\_titled, friend, partner, partner.married, partner.unmarried, mate, mate.senior, mate.junior, boss, subordinate, server, server.clerk, server.doctor, server.nurse, server.police, server.driver, server.other, customer, god, leader, clergy, clergy.Buddhism, clergy.Christianity, clergy.other, follower, follower.quasi\_clergy, follower.other, royal, royal.king, royal.queen, royal.other, commoner|
|Group |foreigner, local, local.indigenous, local.immigrant, local.immigrant.Chinese, local.immigrant.Indian|
|Formality | formal, informal|
|Intimacy | close, remote|
|Number | sg, pl, pl.incl, pl.excl|

## Codes and tags
### Language codes
The [ISO 639-3](https://iso639-3.sil.org) codes are used.
- `jpn` Japanese
- `kor` Korean
- `ind` Indonesian
- `zsm` Malay
- `jav` Javanese
- `tha` Thai
- `vie` Vietnamese
- `myn` Burmese

### Functions
- `1st` speaker reference, first person
- `2nd` addressee reference, second person
- `address` address term
- `title` honorific (and other types of) title

## Judgements
- `yes` acceptable, available, possible
- `no` unacceptable, unavailable, impossible
- `*` acceptable if used together with a title, but not by itself
- `?` uncertain, requires checking
