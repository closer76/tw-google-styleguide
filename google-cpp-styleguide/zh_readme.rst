中文版前言
====================

:版本:   英文版 63107a12eb85a4da33e2585a912234e4794cea06 (2019/5/21 翻譯中)

:原作者:

    .. line-block::

         Benjy Weinberger
         Craig Silverstein
         Gregory Eitzmann
         Mark Mentovai
         Tashana Landray

:翻譯:

    .. line-block::

        `YuleFox <http://www.yulefox.com>`_
        `Yang.Y <https://github.com/yangyubo>`_
        `acgtyrant <http://acgtyrant.com>`_
        `lilinsanity <http://github.com/lilinsanity>`_
        `welkineins <http://github.com/welkineins>`_
        `closer76 <http://github.com/closer76>`_

:專案網頁:

    - `Google Style Guide <https://github.com/google/styleguide>`_
    - `Google 開源專案風格指南 - 簡體中文版 <http://github.com/zh-google-styleguide/zh-google-styleguide>`_
    - `Google 開源專案風格指南 - 繁體中文版 <https://github.com/welkineins/tw-google-styleguide>`_
    - `Google 開源專案風格指南 - 繁體中文版 (forked) <https://github.com/closer76/tw-google-styleguide>`_

譯者前言
--------------------

Google 經常會發佈一些開源專案，意味著會接受來自其他程式碼貢獻者的程式碼。但是如果程式碼貢獻者的程式撰寫風格與 Google 不一致，會給程式碼閱讀者和其他程式碼提交這造成不小的困擾。Google 因此發佈了這份自己的程式撰寫風格指南，使所有提交程式碼的人都能獲知 Google 的程式撰寫風格。

翻譯初衷：

    規則的作用就是避免混亂。但規則本身一定要權威，有說服力，並且是理性的。我們所見過的大部分程式撰寫規範，其內容或不夠嚴謹，或闡述過於簡單，或帶有一定的武斷性。

    Google 保持其一貫的嚴謹精神，5 萬漢字的指南涉及廣泛，論證嚴密。我們翻譯該系列指南的主因也正是其嚴謹性。嚴謹意味著指南的價值不僅僅局限於它羅列出的規範，更具參考意義的是它為了列出規範而做的謹慎權衡過程。

    指南不僅列出你要怎麼做，還告訴你為什麼要這麼做，哪些情況下可以不這麼做，以及如何權衡其利弊。其他團隊未必要完全遵照指南亦步亦趨，如前面所說，這份指南是 Google 根據自身實際情況打造的，適用於其主導的開源專案。其他團隊可以參照該指南，或從中汲取靈感，建立適合自身實際情況的規範。

    我們在翻譯的過程中，收穫頗多。希望本系列指南中文版對你同樣能有所幫助。

我們翻譯時也是盡力保持嚴謹，但水平所限，bug 在所難免。有任何意見或建議，可與我們取得聯繫。

中文版和英文版一樣，使用 ``Artistic License/GPL`` 開源許可。

繁體中文版修訂歷史：

    - 2019-05: @closer76 同步至英文版 63107a12eb85a4da33e2585a912234e4794cea06 。

	- 2016-02: @welkineins 為了撰寫公司內部的程式撰寫風格，將簡體中文版作為基礎將其翻譯為繁體中文，並且修正兩岸間的用語差異，同時也進行了一些細微的敘述調整。
	
簡體中文版修訂歷史：

    - 2015-08：熱心的清華大學同學 @lilinsanity 完善了「類」章節以及其它一些小章節。至此，對 Google CPP Style Guide 4.45 的翻譯正式竣工。

    - 2015-07 4.45：acgtyrant 為了學習 C++ 的規範，順便重新翻譯了本 C++ 風格指南，特別是 C++11 的全新內容。排版大幅度優化，翻譯措辭更地道，添加了新譯者筆記。Google 總部 C++ 工程師 innocentim，清華大學不願意透露姓名的唐馬儒先生，大阪大學大學院情報科學研究科計算機科學專攻博士 farseerfc 和其它 Arch Linux 中文社區眾幫了譯者不少忙，謝謝他們。因為 C++ Primer 尚未完全入門，暫時沒有翻譯「類」章節和其它一些小章節。

    - 2009-06 3.133：YuleFox 的 1.0 版已經相當完善，但原版在近一年的時間裡，其規範也發生了一些變化。

        Yang.Y 與 YuleFox 一拍即合，以專案的形式來延續中文版 : `Google 開源專案風格指南 - 中文版專案 <http://github.com/yangyubo/zh-google-styleguide>`_。

        主要變化是同步到 3.133 最新英文版本，做部分勘誤和改善可讀性方面的修改，並改進排版效果。Yang.Y 重新翻修，YuleFox 做後續評審。

    - 2008-07 1.0：出自 `YuleFox 的 Blog <http://www。yulefox。com/?p=207>`_，很多地方摘錄的也是該版本。
