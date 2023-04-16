# ProSub

## Introduction
This repository contains resources developed by the JSPS KAKENHI project "A cross-linguistic study of pronoun substitutes and address terms" ([JP20H01255](https://kaken.nii.ac.jp/ja/grant/KAKENHI-PROJECT-20H01255/)).

## How to cite
- (Common questionnaire)  
  岡野賢二, 野元裕樹, スニサーウィッタヤーパンヤーノン, トゥザライン, 春日淳. 2022.[「アジア三言語における代名詞代用・呼びかけ語の共通項目調査」](https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/D1-2.pdf)『言語処理学会第28回年次大会発表論文集』, 69-73.
- (Dataset)  
  谷口龍子, 大久保弥, 野元裕樹, 南潤珍. 2022. [「代名詞代用・呼びかけ表現の多言語データセット」](https://www.ls-japan.org/modules/documents/LSJpapers/meeting/164/handouts/p/P-6_164.pdf).『日本言語学会第164回大会予稿集』, 307-313.
- (Annotations)  
  Nomoto, Hiroki, Ryuko Taniguchi, Shiori Nakamura, Yunjin Nam, Sri Budi Lestari, Sunisa Wittayapanyanon (Saito), Virach Sornlertlamvanich, Atsushi Kasuga, Kenji Okano and Thuzar Hlaing. 2023. [Pronoun substitute annotation in seven Asian languages](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P9-4.pdf). _Proceedings of the Twenty-Ninth Annual Meeting of the Association for Natural Language Processing_, 2242-2247.

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
