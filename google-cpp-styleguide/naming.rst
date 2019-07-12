命名約定
------------------

最重要的一致性規則是命名管理。命名風格讓閱讀者可以快速得知名字所代表的類型為何：型別、變數、函式、常數、巨集……等等，甚至不需要去搜尋該名稱的宣告。我們大腦中的樣式比對引擎可以非常可靠的處理這些命名規則。

命名規則具有一定隨意性，但我們認為一致性比個人喜好重要，所以不管你覺得合不合理，規則總歸是規則。

.. _general-naming-rule:

通用命名規則
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    名稱要有描述性；少用縮寫。

命名儘可能有描述性且合理。別心疼空間，畢竟讓新讀者易於理解程式碼更重要。不要用只有專案開發者能理解的縮寫，也不要通過砍掉幾個字母來縮寫單詞。對於沒有參與這個專案、但在相關領域的人熟悉的縮寫字，可以使用。大致上來說，只要該縮寫字在 Wikipedia 上找得到，就 OK。

.. code-block:: c++

    int price_count_reader;    // 無縮寫。
    int num_errors;            // "num" 是很常見的縮寫字。
    int num_dns_connections;   // 大部份的人都知道 "DNS" 是啥。
    int lstm_size;             // "LSTM" 在機器學習領域中是個常用的縮寫字。

.. rst-class:: bad-code
.. code-block:: c++

    int n;                     // 毫無意義。
    int nerr;                  // 模稜兩可的縮寫。
    int n_comp_conns;          // 模稜兩可的縮寫。
    int wgc_connections;       // 只有貴團隊知道是啥意思。
    int pc_reader;             // "pc" 有太多可能的解釋了。
    int cstmr_id;              // 有刪減若干字母。
    FooBarRequestInfo fbri;    // 根本不是個單字。

值得一題的是：某些全世界通用的縮寫字是 OK 的，例如用 ``i`` 當迴圈變數，以及用 ``T`` 當成模板參數。

對於某些符號，這份風格指南建議將第一個字母大寫，同時其後的每一個新的單字首字母均大寫（也就是所謂的「`駝峰式命名/Camel Case <https://en.wikipedia.org/wiki/Camel_case>`_」或稱 "Pascal case"）。當這樣的名稱中出現縮寫字的時候，建議把整個縮寫字當成一個單字，只有首字母大寫。舉例來說，要寫 ``StartRpc()``，而非 ``StartRPC()``。

模板參數應依照它們的分類命名：型別模板參數就應該遵守 :ref:`type-names` 的規則，而非型別的模板參數則應該遵守 :ref:`變數名稱 <variable-names>` 的規則來命名。

.. _file-names:

檔案名稱
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    檔案名稱要全部小寫，可以包含底線 (``_``) 或減號 (``-``)。依專案慣例來選用。如果專案沒有一致的用法，用 "``_``" 比較好。

可接受的檔案命稱範例：

    * my_useful_class.cc
    * my-useful-class.cc
    * myusefulclass.cc
    * muusefulclass_test.cc // ``_unittest`` 和 ``_regtest`` 已棄用。

C++ 檔案要以 ``.cc`` 結尾，標頭檔以 ``.h`` 結尾。供使用者以文字模式引入的檔案則以 ``.inc`` 結尾，參見:ref:`self-contained headers`。

不要使用已經存在於 ``/usr/include`` 下的檔案名稱，如 ``db.h``。

整體來說，應儘量讓檔案名稱更加明確。例如 ``http_server_logs.h`` 就比 ``logs.h`` 要好。定義類別時檔案名稱一般成對出現，例如 ``foo_bar.h`` 和 ``foo_bar.cc``，定義了類別 ``FooBar``。

.. _type-names:

型別名稱
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    型別名稱的每個單字首字母均大寫，不使用底線：``MyExcitingClass``，``MyExcitingEnum``。

所有型別命名（類別、結構、型別別名、列舉，以及模板型別參數）均使用相同規則。型別名稱的第一個字母要大寫，其後每個單字的字首字母均大寫，例如:

.. code-block:: c++

    // 類別和結構
    class UrlTable { ...
    class UrlTableTester { ...
    struct UrlTableProperties { ...

    // typedefs
    typedef hash_map<UrlTableProperties *, string> PropertiesMap;

    // using 別名
    using PropertiesMap = hash_map<UrlTableProperties *, string>;

    // 列舉
    enum UrlTableErrors { ...

.. _variable-names:

變數名稱
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    變數（包括函式的參數）以及資料成員的名稱一律小寫，單字之間用底線連接。類別的資料成員結尾處多加一個底線（但結構的資料成員不用），如：``a_local_variable``、``a_struct_data_member``、``a_class_data_member_``。

一般變數命名：

    範例：

    .. code-block:: c++

        string table_name;  // 可 - 用底線。
        string tablename;   // 可 - 全小寫。

    .. rst-class:: bad-code
    .. code-block:: c++

        string tableName;   // 差 - 混合大小寫。

類別資料成員：

    不管是靜態的還是非靜態，類別資料成員的命名方式和普通變數一樣，但最後要加上底線。

    .. code-block:: c++

        class TableInfo {
            ...
            private:
            string table_name_;  // 可 - 字尾加底線。
            string tablename_;   // 可。
            static Pool<TableInfo>* pool_;  // 可。
        };

結構資料成員：

    不管是靜態的還是非靜態，結構資料成員的命名方式和普通變數一樣。不用像類別那樣最後加底線。

    .. code-block:: c++

        struct UrlTableProperties {
            string name;
            int num_entries;
        }

    關於何時該用結構、何時該用類別的討論，請參考 :ref:`structs-vs-classes` 一節。

.. _constant-names:

常數名稱
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    宣告時加上 ``constexpr`` 或 ``const``，且整個程式執行時間內都不會改變的變數，命名時需以 "k" 開頭，後面的字母以混合大小寫的方式書寫。在少數大寫字無法將單字隔開的情況下，可以使用底線當作區隔。舉例來說：

    .. code-block:: c++

        const int kDaysInAWeek = 7;
        const int kAndroid8_0_0 = 24;  // Android 8.0.0

所有這類的變數，若擁有靜態儲存週期（也就是靜態和全域變數，細節請參考 `靜態儲存週期 (static storage duration) <http://en.cppreference.com/w/cpp/language/storage_duration#Storage_duration>`__）的話，必須以此規則命名。其他儲存週期的變數（例如自動變數）不一定要套用這個規則，可以使用一般變數的命名原則。

.. _function-names:

函式名稱
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    一般函式使用大小寫混合，取值和設值函式則可以用類似變數的方式命名。

一般來說，函式名稱的第一個字母要大寫，其後每個單字的字首字母均大寫。

.. code-block:: c++

    AddTableEntry()
    DeleteUrl()
    OpenFileOrDie()

（在類別以及命名空間作用域中宣告、並被當成 API 的一部份輸出的常數，命名方式和函式相同。這是為了讓這些常式看起來很像函式，因為在實作上，它們到底是物件還是函式，其實並不是很重要。）

取值和設值函式可以按照變數的方式命名。通常這樣命名時，會跟實際上的成員變數對應，但沒有一定要這麼做。例如 ``int count()`` 和 ``void set_count(int count)``。

.. _namespace-names:

命名空間名稱
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    命名空間用小寫字母命名。最上層的命名空間名稱需依專案名稱命名。儘可能不要讓名稱和巢狀結構內的命名空間、或是其他廣為人知的最上層命名空間名稱衝突。

最上層的命名空間通常以專案或是團隊（如果這個命名空間中放的是他們的程式碼）名稱命名。該命名空間的程式碼通常會放在名稱和命名空間相同的目錄（或其中的子目錄）中。

要記住：命名空間的名稱和變數名稱一樣，不得違反「:ref:`避免使用不當的縮寫 <general-naming-rule>`」的原則。放在命名空間中的程式碼不太需要冠上命名空間的名稱，因此通常沒有特別需要縮寫。

在命名空間內部的命名空間（即為「巢狀結構內的命名空間，nested namespace」）要避免和其他廣為人知的「最上層命名空間」名稱相同。命名空間名稱衝突可能會因為名稱查尋規則而造成預期之外的編譯中斷。特別是：不要命名空間內部建立 ``std`` 命名空間。儘量使用專案內獨有的名稱（如 ``websearch::index``、``websearch::index_util``），而不要用那些可能造成衝突的名稱（如 ``websearch::util``）。

在使用 ``internal`` 命名空間時，要小心其他加入同一個 ``internal`` 命名空間的程式碼所造成的衝突（在團隊中所建立的內部輔助函式常會用上相同的名稱，導致衝突的發生）。在這種情況下，把檔案名稱加到名稱中，可以有效建立獨一無二的名稱（例如 在 ``frobber.h`` 中，就用 ``websearch::index::frobber_internal`` 這樣的名稱）。

.. _enumerator-names:

列舉元 (Enumerator) 名稱
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    列舉元（不管是否有限定範圍）的命名應當和 :ref:`常數 <constant-names>` 或 :ref:`巨集 <macro-names>` 一致：可以是 ``kEnumName`` 或是 ``ENUM_NAME``。

單獨的列舉元應該優先採用 :ref:`常數 <constant-names>` 的命名方式。但 :ref:`巨集 <macro-names>` 方式的命名也可以接受。列舉型別 (enumeration) 像是 ``UrlTableErrors`` （以及 ``AlternateUrlTableErrors``）是型別，因此要用大小寫混合的方式命名。

.. code-block:: c++

    enum UrlTableErrors {
        kOK = 0,
        kErrorOutOfMemory,
        kErrorMalformedInput,
    };
    enum AlternateUrlTableErrors {
        OK = 0,
        OUT_OF_MEMORY = 1,
        MALFORMED_INPUT = 2,
    };

2009 年 1 月之前，我們一直建議採用 :ref:`巨集 <macro-names>` 的方式為列舉值命名。這導致列舉值和巨集之間的命名衝突問題。因此，這裡改為優先選擇常數風格的命名方式。新的程式碼應儘可能優先使用常數風格。但是原有的程式碼沒有一定要轉換到常數風格，除非巨集風格確實會在編譯時產生問題。

.. _macro-names:

巨集名稱
~~~~~~~~~~~~~~~~~~

.. tip::

    你不是真的想 :ref:`使用巨集 <preprocessor-macros>`，對吧？如果你一定要用，命名風格應如： ``MY_MACRO_THAT_SCARES_SMALL_CHILDREN_AND_ADULTS_ALIKE``。

請參考 :ref:`巨集一節的描述 <preprocessor-macros>`；一般來說 *不應該* 使用巨集。如果不得不用，其命名應為全部大寫，並使用底線區隔單字：

.. code-block:: c++

    #define ROUND(x) ...
    #define PI_ROUNDED 3.0

.. _exceptions-for-naming-rules:

命名規則的特例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    如果你命名的名稱與現有 C/C++ 已有的名稱相似，可參考現有命名策略。

``bigopen()``
    函式名，參考 ``open()`` 的格式

``uint``
    ``typedef``

``bigpos``
    ``struct`` 或 ``class``，參考 ``pos`` 的格式

``sparse_hash_map``
    STL 相似的名稱；參考 STL 命名約定

``LONGLONG_MAX``
    常數，類似於 ``INT_MAX``
