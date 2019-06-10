註解
------------

註解雖然寫起來很痛苦，但對於確保程式碼的可讀性至關重要。下面的規則描述了如何註解、以及在哪兒註解。當然也要記住：註解固然很重要，但最好的程式碼本身應該要能自我說明。有意義的型別名稱和變數名稱，遠勝於要用註解解釋的含糊不清的名稱。

你寫的註解是給程式碼閱讀者看的，也就是下一個需要理解你的程式碼的人。慷慨些吧，下一個人可能就是你！

註解風格
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    使用 ``//`` 或 ``/* */``，只要一致就好。

``//`` 或 ``/* */`` 都可以；但 ``//`` *更* 常用。註解方式及註解風格須保持一致。

檔案註解
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    在每一個檔案開頭加入授權 (license) 宣告。

    檔案註解描述了檔案的內容。如果一個檔案中只有單一的項目的宣告、實作，或測試，且該項目的宣告之處已經有註解的話，那麼檔案註解可以省略。在其他的情況下，檔案一律需要檔案註解。

法律公告和作者資訊：

    每個檔案都應有授權宣告。依專案所使用的授權（例如 Apache 2.0、BSD、LGPL、GPL），選擇適當的授權宣告。

    如果你對已有作者資訊的檔案做了重大的修改，可以考慮刪除原有的作者資訊。新增的檔案通常不會有版權 (copyright) 與作者資訊。

檔案內容：

    如果一個 ``.h`` 檔中宣告了數個不同的項目，檔案註解應該要能概括地描述檔案的內容，以及這些項目的關聯性為何。檔案註解大約一、兩行應該就夠了。個別項目的詳細說明應該跟著那些項目跑，而不是放在檔案頂端。

    不要直接在 ``.h`` 和 ``.cc`` 間複製註解。複製的註解無法同步管理。

.. _class-comments:

類別註解
~~~~~~~~~~~~~~~~~~

.. tip::

    每個非一望即知的類別宣告處都要附帶一份註解，描述類別的功能和用法。

.. code-block:: c++

    // 範例：
    // Iterates over the contents of a GargantuanTable.  Sample usage:
    //    GargantuanTable_Iterator* iter = table->NewIterator();
    //    for (iter->Seek("foo"); !iter->done(); iter->Next()) {
    //      process(iter->key(), iter->value());
    //    }
    //    delete iter;
    class GargantuanTable_Iterator {
        ...
    };

類別的註解應該要提供給程式碼閱讀者足夠的資訊，了解如何使用、何時該使用這個類別，以及任何想要正常使用這個類別所需要考慮到的額外事項。如果該類別有任何同步前提 (synchronization assumptions)，請詳細說明。如果該類別的實例可被多執行緒存取，要特別註明多執行緒環境下相關的規則和常數使用。

類別註解內很適合放一段簡短的範例程式，聚焦在簡單地示範該類別的使用方法。

若宣告和定義分別放在 ``.h`` 和 ``.cc`` 檔中，描述類別使用法的註解應該要放在介面的宣告之處；而說明類別運作以及實作方法的註解應該要放在類別成員函式的實作之處。

函式註解
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    若是函式的用法非顯而易見，那麼就在函式宣告處加上用法說明的註解；函式詳細運作相關的註解放在函式定義處。

函式宣告：

    幾乎每個函式在宣告之前都應該有註解，描述其功能及用法。若是函式很簡單且一望即知其功能（例如：單純讀取類別屬性的存取函式），則其註解可以省略。註解使用敘述句 ("Opens the file") 而非命令語句 ("Open the file")；註解只是為了描述函式，而不是命令函式做什麼。通常放在宣告處的註解不會描述函式如何工作。描述工作原理的註解應放在函式定義處。

    函式宣告處註解的內容：

        - 函式的輸入輸出。
        - 針對類別成員函式：物件在函式呼叫之後是否會保存 reference 引數、是否之後會釋放這些參數。
        - 函式是否會配置需要由呼叫端負責釋放記憶體。
        - 引數是否可為 null 指標。
        - 若函式使用不當是否會有性能隱憂。
        - 函式是否可以遞迴呼叫 (re-entrant)。其同步前提是什麼？

    舉例如下:

        .. code-block:: c++

            // Returns an iterator for this table.  It is the client's
            // responsibility to delete the iterator when it is done with it,
            // and it must not use the iterator once the GargantuanTable object
            // on which the iterator was created has been deleted.
            //
            // The iterator is initially positioned at the beginning of the table.
            //
            // This method is equivalent to:
            //    Iterator* iter = table->NewIterator();
            //    iter->Seek("");
            //    return iter;
            // If you are going to immediately seek to another place in the
            // returned iterator, it will be faster to use NewIterator()
            // and avoid the extra seek.
            Iterator* GetIterator() const;

    但也要避免過度說明，或是為顯而易見的事實加上不必要的說明。

    當你為覆寫的函式加上註解時，把重點放在新增的功能上，不要把被覆寫的那個函式的註解複製過來。在許多情況下，覆寫版本不需要額外的說明，此時就不必畫蛇添足硬加註解了。

    在為建構式/解構式加註解時，切記閱讀程式碼的人知道構造式/解構式是做什麼用的，所以 "destroys this object（摧毀這個物件）" 這樣的註解是沒有意義的。註明建構式會對參數做些什麼事（例如：是否取得指標所有權）以及解構式清理了什麼。如果都是些無關緊要的內容，直接省掉註解。在標頭檔中，解構式前沒有註解是很正常的。

函式定義：

    如果你的函式使用了什麼特別的技巧完成任務，在定義處要用註解詳細說明。像是你用的程式撰寫技巧、實作的大致步驟，或解釋為何要用這個方法而不是另一種方法。例如你可能會提到為什麼在函式的前半段需要取得鎖定、但後半段又不用。

    *不要* 從 ``.h`` 文件或其他地方的函式宣告處直接複製註解。簡要重述函式功能是可以的，但註解重點要放在如何實作上。

變數註解
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    通常變數名本身足以很好說明變數的用途。某些情況下，還是需要額外的註解說明。

類別資料成員：

    類別中每個資料成員（也被稱為「實例變數」或「成員變數」）的目的必須非常清楚。如果有任何無法以型別或名稱清楚表達的事實（特殊的數值、成員間的關係、生命週期需求等），就必須為之加上註解。然而，若是型別和名稱所擁有的資訊已經足夠（``int num_events_;``），那就不需要額外加註解了。

    特別是若存在某些被拿來當成特殊狀況的數值（像是 ``nullptr`` 或是 ``-1``）而且又不是顯而易見的話，就要特別為它們加上註解。例如：
    
        .. code-block:: c++

            private:
              // Used to bounds-check table accesses. -1 means
              // that we don't yet know how many entries the table has.
              int num_total_entries_;


全域變數：

    所有的全域變數都要註解說明含義、用途，以及為什麼要將它宣告為全域變數（如果不夠清楚的話）。例如：

        .. code-block:: c++

            // The total number of tests cases that we run through in this regression test.
            const int kNumTestCases = 6;

實作註解
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    對於程式碼中巧妙的、晦澀的、有趣的，或重要的地方加以註解。

解釋用註解：

    巧妙或複雜的程式碼段前要加註解。例如：

        .. code-block:: c++

            // Divides result by two, taking into account that x
            // contains the carry from the add.
            for (int i = 0; i < result->size(); i++) {
                x = (x << 8) + (*result)[i];
                (*result)[i] = x >> 1;
                x &= 1;
            }

行註解：

    同時，比較隱晦的地方要在行尾加入註解。在行尾加兩格空隔後開始註解。例如：

        .. code-block:: c++

            // If we have enough memory, mmap the data portion too.
            mmap_budget = max<int64>(0, mmap_budget - index_->length());
            if (mmap_budget >= data_size_ && !MmapData(mmap_chunk_bytes, mlock))
                return;  // Error already logged.

    可以看到這裡用了兩段註解分別描述這段程式碼的作用，而且在函式返回時也有註解，說明錯誤已經被記入日誌。

    如果你需要連續進行多行註解，使之對齊可以讓可讀性更高：

        .. code-block:: c++

            DoSomething();                  // 把註解放這裡才能和下一行對齊。
            DoSomethingElseThatIsLonger();  // 註解和程式碼之間要有兩個空格。
            { // 當開啟一個新的作用域時，可以只放一個空隔，
              // 這樣接下來的註解和程式碼都可以和前面那行對齊。
              DoSomethingElse();  // 一般來說行註解前面都需要兩個空隔。
            }
            std::vector<string> list{
                                // 在條列初始化中，用來說明下一個元素的註解...
                                "First item",
                                // .. 必須要妥善對齊。
                                "Second item"};
            DoSomething(); /* 對於放在行尾的區塊式註解，可以只放一個空隔。 */

函式引數註解：

    當函式的引數意義不那麼明顯時，可以考慮以下的補救措施：
    
        - 如果引數是字面常數 (literal constant)，在許多函式呼叫的時候都會被引用到，而且在這些地方意義都相同時，你應該要建立一個有名稱的常數，明確地表明它的限制，且保證呼叫的時候不會給錯值。
        - 考慮改變函式傳入值的型別，把 ``bool`` 引數改成 ``enum`` 引數。如此一來引數的值就能自我描述了。
        - 如果函式有許多設定選項，可以考慮把這些選項全都包進一個類別或結構中，然後傳遞這個型別的實例。這種方法有許多的好處。選項在呼叫處就有名稱可以參考，它們代表的意義就非常清楚了。另外函式所需要的引數數量變少了，函式呼叫變得更易讀也更易寫。還有一個額外的好處就是：如果你要再加上一個新的選項，呼叫端不用特別去修改。
        - 將龐大或複雜的巢狀表達式換成有名字的變數。
        - 若是上述的方法都不管用，才考慮在呼叫端使用註解說明引數的意義。

    考慮以下的範例：

        .. code-block:: c++

            // 這些引數代表的意義是什麼？
            const DecimalNumber product = CalculateProduct(values, 7, false, nullptr);

    對照組：

        .. code-block:: c++

            ProductOptions options;
            options.set_precision_decimals(7);
            options.set_use_cache(ProductOptions::kDontUseCache);
            const DecimalNumber product =
                CalculateProduct(values, options, /*completion_callback=*/nullptr);

不要這麼做：

    不要陳述顯而易見的事實。特別是不要依字面去翻譯程式碼在幹嘛，除非它的行為對於熟悉 C++ 的閱讀者來說不是那麼直觀的。應該要提提供更高階的註解，來描述這段程式碼為什麼要這麼做，或是想辦法讓程式碼可以自我描述。

    比較這個範例：

        .. code-block:: c++

            // Find the element in the vector.  <-- 不好：不用說也知道！
            auto iter = std::find(v.begin(), v.end(), element);
            if (iter != v.end()) {
              Process(element);
            }

    和這個範例：

        .. code-block:: c++

            // Process "element" unless it was already processed.
            auto iter = std::find(v.begin(), v.end(), element);
            if (iter != v.end()) {
              Process(element);
            }

    可以自我描述的程式碼不需要註解。上面那段程式碼若以這種方式寫成，就不需要註解了：

        .. code-block:: c++

            if (!IsAlreadyProcessed(element)) {
              Process(element);
            }

標點、拼寫和文法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    注意標點、拼寫和語法；寫得好的註解比差的要易讀的多。

註解必須易讀且平舖直述，適當使用大小寫和標點符號。通常完整的語句比片斷的字句更易讀。短一點的註解（如程式碼行尾註解）可以隨性點，但風格仍必須保持一致。

雖然被別人指出該用分號時卻用了逗號多少有些尷尬，但清晰易讀的高品質程式碼還是很重要的。正確的標點、拼寫和文法對此會有所幫助。

TODO 註解
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    在那些臨時的、短期的解決方案，或已經夠好但仍不完美的程式碼旁加上 ``TODO`` 註解。

``TODO`` 註解要使用全大寫的字串 ``TODO``，在隨後的圓括號裡寫上你的大名、郵件地址、bug ID，或其他最能說明這項 ``TODO`` 的身份標識、問題資訊等。主要目的是建立一致的 ``TODO`` 格式，讓閱讀程式的人可以依這些資訊找到更多關於這項要求的細節。``TODO`` 並不代表解決這個問題的承諾。因此建立 ``TODO`` 時所加上的名字，幾乎 100% 是建立者的名字。

    .. code-block:: c++

        // TODO(kl@gmail.com): Use a "*" here for concatenation operator.
        // TODO(Zeke) change this to use relations.
        // TODO(bug 12345): remove the "Last visitors" feature

如果加 ``TODO`` 是為了在「將來某一天做某事」，可以附上一個非常明確的時間 ("Fix by November 2005")，或者一個明確的事項 ("Remove this code when all clients can handle XML responses.")。

棄用 (deprecation) 註解
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    若是某界面已被棄用，用 ``DEPRECATED`` 註解標記該界面。

你可以寫上包含全大寫的 ``DEPRECATED`` 的註解，以標記某界面為棄用狀態。註解可以放在界面宣告前，或者同一行。

在 ``DEPRECATED`` 一詞後，留下你的名字，電子郵件地址或其他可供識別的文字（用括號括起來）。

棄用註解中必須要有簡單且清楚的指示，說明使用者該如何修改呼叫端的程式碼。在 C++ 中，你可以將棄用函式實作為呼叫新版界面的 inline 函式。

僅僅標記界面為 ``DEPRECATED`` 並不會讓呼叫端的程式碼自動修正。如果你希望真的停用被棄用的界面，你得親自主動修正呼叫端的程式碼，或是找人幫忙修正。

新增的程式碼不得再使用已被棄用的界面，應改用新的界面。如果你不知道該怎麼改，可以問當初加上棄用註解的人新的界面該如何使用。
