# ProSub

## Introduction
This repository contains resources developed by the JSPS KAKENHI project "A cross-linguistic study of pronoun substitutes and address terms" ([JP20H01255](https://kaken.nii.ac.jp/ja/grant/KAKENHI-PROJECT-20H01255/)).

## How to cite
```
@proceedings{OkanoEtAl22,
    author = {Okano, Kenji and Nomoto, Hiroki and Wittayapanyanon, Sunisa and Thuzar Hlaing and Kasuga, Atsushi},
    year = {2022},
    title = {Ajia sangengo niokeru daimeishidaiyou, yobikakego no kyoutsuukoumoku chousa},
    booktitle = {Proceedings of the Twenty-Eighth Annual Meeting of the {A}ssociation for {N}atural {L}anguage {P}rocessing},
    pages = {##-##},
    note = {An investigation of pronoun substitutes and address terms in three Asian languages based on a common questionnaire},
    }
```

## Contents
- `common_questionnaire.tsv` A common questionnaire for investigating pronoun substitutes and address terms
- `data_all_v1.0.tsv` Data in Japanese, Korean, Indonesian, Malay, Javanese, Thai, Vietnamese and Thai in the tag-separated format.  English translations are not complete.  Ensure that the encoding is set as UTF-8 when you open the file with MS Excel.
- `data_all_v1.0.json` Data in Japanese, Korean, Indonesian, Malay, Javanese, Thai, Vietnamese and Thai in the json format.  English translations are not complete.

## Format
### common_questionnaire.tsv
`ID [TAB] concept (Japanese) [TAB] concept (English) [TAB] WordNet synset ID [TAB] semantic category`

The semantic categories are based on the [feature system](https://github.com/matbahasa/TALPCo/blob/master/features.pdf) proposed by:  
Nomoto, Hiroki, Kenji Okano, Sunisa Wittayapanyanon and Junta Nomura. 2019. [Interpersonal meaning annotation for Asian language corpora: The case of TUFS Asian Language Parallel Corpus (TALPCo)](https://www.anlp.jp/proceedings/annual_meeting/2019/pdf_dir/D4-4.pdf).  _Proceedings of the Twenty-Fifth Annual Meeting of the Association for Natural Language Processing_, 846-849.

### data_all_v1.0.tsv
`language code [TAB] concept ID [TAB] concept (Japanese) [TAB] concept (English) [TAB] semantic category [TAB] expression [TAB] Japanese translation of expression [TAB] English translation of expression [TAB] function [TAB] judgement [TAB] example [TAB] Japanese translation of example [TAB] English translation of example [TAB] source [TAB] notes`

### data_all_v1.0.json
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

## Codes and tags
### Language codes
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
- `*` acceptable if a title is added, but not by itself
- `?` uncertain, requires cheking
