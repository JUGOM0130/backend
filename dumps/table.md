# マスタテーブル構成

## <div style="color:#FF5">社員テーブル　「m_staff」</div>
|PK|カラム名|カラム名|型|桁数|その他|
|:-:|:--|:--|:--|:--|:--|
|＊|scode|社員番号|INT||AI|
||sname1|氏|VARCHAR|45|NN|
||sname2|名|VARCHAR|45|NN|
||sname3|氏（カナ)|VARCHAR|45||
||sname4|名（カナ）|VARCHAR|45||
||toroku|登録日|DATEDATETIME||NN CURRENT_TIMESTAMP|
||kosin|更新日|DATEDATETIME||NN CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP|

## <div style="color:#FF5">コードテーブル　「m_code」</div>
|PK|カラム名|カラム名|型|桁数|その他|
|:-:|:--|:--|:--|:--|:--|
|＊|ctid|テーブルID|INT||AI NN|
||ctkind|コード種別|INT||1=組　2=部品　3=購入品|
||cthead|コードヘッダ|VARCHAR|10||
||ctenumber|英番|VARCHAR|5||
||ctnumber|番号|INT|||
||ctfoot|コードフッタ|VARCHAR|10||
||toroku|登録日|DATEDATETIME||NN CURRENT_TIMESTAMP|
||kosin|更新日|DATEDATETIME||NN CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP|

## <div style="color:#FF5">パーツテーブル「m_parts」</div>
|PK|カラム名|カラム名|型|桁数|その他|
|:-:|:--|:--|:--|:--|:--|
|＊|pid|テーブルID|INT||AI NN|
|FK|pctid|m_code.ctid|INT||外部キー　m_code.ctid|
||pcd|パーツコード|VARCHAR|45||
||pname|パーツ名|VARCHAR|45||
||ppname|パーツ名称|VARCHAR|45||
||prevision|改版番号|VARCHAR|45||
||pvendor|手配先|VARCHAR|45||
||ptype|型式|VARCHAR|45||
||pmaterial|材質|VARCHAR|45||
||pio|内外策|VARCHAR|45|1=内策　2=外策　3=内外策|
||pmtlmain_cost|主要材料費|INT|||
||pmtlsub_cost|補助材料費|INT|||
||pprocdict_cost|外注加工費|INT|||
||pprocsub_cost|直接労務費|INT|||
||toroku|登録日|DATEDATETIME||NN CURRENT_TIMESTAMP|
||ptype|更新日|DATEDATETIME||NN CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP|
