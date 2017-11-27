"""
    Samples for converting between Hankaku and Zenkaku (Japanese Chars).

    Requirements:
        - https://github.com/studio-ousia/mojimoji
"""
import mojimoji

#
# Zenkaku to Hankaku
#

print(mojimoji.zen_to_han("アイウエオ１２３４５ＡＢＣ"))
# => ｱｲｳｴｵ12345ABC

print(mojimoji.zen_to_han("アイウエオ１２３４５ＡＢＣ", kana=False))
# => アイウエオ12345ABC

print(mojimoji.zen_to_han("アイウエオ１２３４５ＡＢＣ", digit=False))
# => ｱｲｳｴｵ１２３４５ABC

print(mojimoji.zen_to_han("アイウエオ１２３４５ＡＢＣ", ascii=False))
# => ｱｲｳｴｵ12345ＡＢＣ


#
# Hankaku to Zenkaku
#

print(mojimoji.han_to_zen("ｱｲｳｴｵ12345abc"))
# => アイウエオ１２３４５ａｂｃ

print(mojimoji.han_to_zen("ｱｲｳｴｵ12345abc", kana=False))
# => ｱｲｳｴｵ１２３４５ａｂｃ

print(mojimoji.han_to_zen("ｱｲｳｴｵ12345abc", digit=False))
# => アイウエオ12345ａｂｃ

print(mojimoji.han_to_zen("ｱｲｳｴｵ12345abc", ascii=False))
# => アイウエオ１２３４５abc


