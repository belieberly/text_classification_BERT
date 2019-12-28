# text_style_classification_BERT

在BERT开源的中文模型的基础上，使用部分自己的数据做finetune

具体操作步骤见 https://github.com/kuhung/bert_finetune 

## 步骤

在训练和测试数据集中加入judicial数据集

完成分类模型的训练和预测

## 操作方法

运行命令在shell_input中，分为训练和预测

结果在tmp中

## 结果

1228--整段文本分类精确度很好，但是如何使用还有待考虑，要细化文本粒度，分句或者分段，数据集也需要扩增，数据量太小。并且数据相关度太小，没有说服力。



## TODO

学习文本风格后，对原始裁判文书进行风格迁移得到新的数据集，重新使用本方法。



