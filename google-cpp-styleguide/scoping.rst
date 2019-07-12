作用域 (Scoping)
---------------------

.. _namespaces:

命名空間 (Namespaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    除了少數的例外，都建議使用把程式碼放在命名空間內。一個具名的命名空間應該擁有唯一的名字，其名稱可基於專案名稱，甚至是相對路徑。禁止使用 using 指令 (using-directives)。禁止使用行內命名空間 (inline namespaces)。至於匿名的命名空間 (unnamed namespace)，請參閱 :ref:`unmamed-namespaces-and-static-variable` 一節。

定義：

    命名空間將全域作用域細分為獨立的、具名的作用域，可有效防止全域作用域的命名衝突。

優點：

    命名空間可以在大型專案內避免名稱衝突，同時又可以讓多數的程式碼有合理簡短的名稱。

    舉例來說, 兩個不同專案的全域作用域都有一個類別 ``Foo``，這樣在編譯或運行時期會造成衝突。如果每個專案將程式碼置於不同命名空間中，``project1::Foo`` 和 ``project2::Foo`` 在專案中就可以被視為不同的 symbols 而不會發生衝突。兩個類別在各自的命名空間中，也可以繼續使用 ``Foo`` 而不需要前綴命名空間。

    行內命名空間會自動把內部的名稱放到外層作用域，比如：

    .. code-block:: c++

        namespace outer {
        inline namespace inner {
        void foo();
        }  // namespace inner
        }  // namespace outer

    ``outer::inner::foo()`` 與 ``outer::foo()`` 彼此可以互換使用。行內命名空間主要用來保持跨版本的 ABI 相容性。

缺點：

    命名空間可能讓人感到困惑，因為它增加了識別一個名稱所代表的意義的難度。

    行內命名空間更是容易令人疑惑，因為它無法把名稱限制在所定義的命名空間中。行內命名空間只在某些大型版本控管時會被用到。

    在某些狀況中，經常會需要重複的使用完整 (fully-qualified) 的名稱來參考某些 symbols。對於多層巢狀的命名空間，這會增加許多混亂。

結論：

    應根據以下原則使用命名空間：

    * 遵守 :ref:`namespace-names` 中所定的規則。
    * 在命名空間結束的地方，依下列範例中的方式加上註解。
    * 在 ``include``、`gflags <https://gflags.github.io/gflags/>`_ 的宣告/定義，以及其他命名空間的類別前置宣告之後，把整個原始碼文件放置在命名空間內：

      .. code-block:: c++

        // 在 .h 檔中
        namespace mynamespace {

        // 所有的宣告都都置於命名空間中。
        // 注意不要使用縮排
        class MyClass {
            public:
            ...
            void Foo();
        };

        }  // namespace mynamespace

      .. code-block:: c++

        // 在 .cc 檔中
        namespace mynamespace {

        // 函式定義都置於命名空間中。
        void MyClass::Foo() {
            ...
        }

        }  // namespace mynamespace

      更複雜的 ``.cc`` 檔中可能有更多的細節，例如 flags 或是 using 宣告式。

      .. code-block:: c++

        #include "a.h"

        DEFINE_FLAG(bool, someflag, false, "dummy flag");

        namespace mynamespace {

        using ::foo::bar;

        ...code for mynamespace...    // 程式碼從最左邊開始寫起

        }  // namespace mynamespace

    * 要將程式產生的 protocol message code 放進命名空間中，請在 ``.proto`` 檔中使用  ``package`` 指示詞。詳細說明請見 `Protocol Buffer Packages <https://developers.google.com/protocol-buffers/docs/reference/cpp-generated#package>`_。

    * 不要在命名空間 ``std`` 內宣告任何東西，包括標準函式庫的類別前置宣告。在 ``std`` 命名空間宣告任何東西其結果未定義；也就是說這樣的做法無法移植。要宣告標準函式庫內的實體，直接 ``include`` 對應的標頭檔。

    * 不要使用 using 指令 (using-directive) 讓一個命名空間下的所有名稱都可以使用。

      .. rst-class:: bad-code
      .. code-block:: c++

        // 禁止 —— 這會污染命名空間
        using namespace foo;

    * 不要在標頭檔的命名空間作用域中使用 *命名空間別名* （除非是僅在內部使用且有明確標示的命名空間），因為在標頭檔內的命名空間中匯入的任何東西，都會變成這個檔案所匯出的公開 API 的一部份。

      .. code-block:: c++

        // 在 .cc 檔中，縮短某些常用的名稱。
        namespace baz = ::foo::bar::baz;

      .. code-block:: c++

        // 在 .h 檔中，縮短某些常用的名稱。
        namespace librarian {
        namespace impl {  // 僅供內部使用，非 API 的一部份。
        namespace sidetable = ::pipeline_diagnostics::sidetable;
        }  // namespace impl

        inline void my_inline_function() {
            // 僅在函式（或方法）內使用的命名空間別名。
            namespace baz = ::foo::bar::baz;
            ...
        }
        }  // namespace librarian

    * 禁止使用行內命名空間。

.. _unmamed-namespaces-and-static-variable :

匿名命名空間 (Unnamed Namespaces) 與 Static 變數
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    若是某些定義不會在一個 ``.cc`` 檔以外的地方用到時，可以把那些定義放在匿名命名空間中，或是加上 ``static`` 修飾字。不要在 ``.h`` 檔中使用相同的技巧。

定義：

    所有宣告在匿名命名空間中的符號都只會產生內部連結 (internal linkage)。函式和變數也可以在宣告時加上 ``static`` 修飾字成為內部連結。所有宣告為內部連結的符號都無法被其他的檔案存取。就算另一個檔案中出現了相同的名稱，這兩者仍各自獨立，互不干擾。

結論：

    在 ``.cc`` 檔中，若是某段程式碼不會被其他的檔案參考到，應該儘量讓它成為內部連結。不要在 ``.h`` 檔中產生內部連結。

    匿名命名空間的格式和一般命名空間相同。結束時的註解處不需加上命名空間的名稱：

    .. code-block:: c++

        namespace {
        ...
        }  // namespace

非成員函式、靜態 (Static) 成員函式和全域函式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    建議將非成員函式放置在命名空間中，儘量不要使用完全的全域函式。不要把類別當作將一堆靜態函式打包的工具。類別的靜態方法一般來說要和類別的實例或類別的靜態資料有緊密的關連。

優點：

    某些情況下，非成員函式和靜態成員函式是非常有用的。將非成員函式放在命名空間內可避免對於全域作用域污染。

缺點：

    為非成員函式和靜態成員函式準備一個新的類別可能更有意義，特別是它們需要存取外部資源或式有大量的相依性關係時。

結論：

    有時候定義一個不綁定特定類別實例的函式是有用的，甚至是必要的。這樣的函式可以被定義成靜態成員或是非成員函式。非成員函式不應該依賴於外部變數，且應該總是放置於某個命名空間內。不要單純為了封裝靜態成員函式而創建一個類別；這樣跟單純在函式前面加上前綴字沒什麼兩樣，這樣的封裝通常沒什麼用。

    如果你定義了非成員函式，又只是在 ``.cc`` 文件中使用它，則可使 :ref:`內部連結 <unmamed-namespaces-and-static-variable>` 限定其作用域。

區域變數
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    儘可能將函式內的變數的作用域最小化，並在變數宣告時進行初始化。

C++ 允許在函式內的任何位置宣告變數。我們鼓勵在儘可能小的作用域中宣告變數，並且離第一次使用的地方越近越好。這會讓閱讀者更容易找到變數宣告的位置、宣告的類型和初始值。要注意，應該在宣告時直接初始化變數，而不要先宣告後再賦值, 例如：

.. rst-class:: bad-code
.. code-block:: c++

    int i;
    i = f(); // 不推薦 -- 初始化和宣告分離

.. code-block:: c++

    int j = g(); // 推薦 -- 宣告時初始化

.. rst-class:: bad-code
.. code-block:: c++

    std::vector<int> v;
    v.push_back(1); // 建議使用 {} 初始化法語法
    v.push_back(2);

.. code-block:: c++

    std::vector<int> v = {1, 2}; // 推薦 -- v 在宣告時初始化

在 ``if``、``while`` 和 ``for`` 陳述句需要的變數一般都會宣告在這些陳述句中，也就是這些變數會存活於這些作用域內。例如：

.. code-block:: c++

    while (const char* p = strchr(str, '/')) str = p + 1;

一個特例：如果變數是一個物件，每次進入作用域時其建構式都會被呼叫，每次離開作用域時其解構式都會被呼叫。

.. rst-class:: bad-code
.. code-block:: c++

    // 沒效率的實作
    for (int i = 0; i < 1000000; ++i) {
      Foo f; // 建構式和解構式分別呼叫 1000000 次。
      f.DoSomething(i);
    }

在迴圈作用域外面宣告這類型的變數可能更加的有效率。

.. code-block:: c++

    Foo f; // 建構式和解構式只呼叫 1 次
    for (int i = 0; i < 1000000; ++i) {
      f.DoSomething(i);
    }

.. _static-and-global-variables:

靜態和全域變數
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    禁止使用具有 `靜態儲存週期 (static storage duration) <http://en.cppreference.com/w/cpp/language/storage_duration#Storage_duration>`__ 的物件，除非該物件的型別具有 `trivially
    destructible <http://en.cppreference.com/w/cpp/types/is_destructible>`__ 的特性。以非正式的說法來說，這表示這個物件（包括其所有成員以及基底類別）的解構式不需做任何事。正式一點的說法是：這個型別沒有使用者自訂的解構式、沒有虛擬解構式，而且所有的基底類別及非靜態成員也都是 trivially destructible。函式內的靜態區域變數可以使用動態初始化。我們不鼓勵對類別的靜態成員或命名空間作用域中的變數執行動態初始化，不過某些特例下是允許的，詳見下文。

    從經驗法則來看，考慮一個獨立的全域變數，若是可以宣告為 ``constexpr``，那麼它便滿足這些條件。

定義：

    每個物件都有自己的 *儲存週期* ，和它的生命週期息息相關。擁有靜態儲存週期的物件存活的時間，從它被初始化開始，到程式結束前才終止。這樣的物件可能存在於命名空間作用域（也就是「全域變數」），可能是類別的靜態資料成員，也可能是加上 ``static`` 修飾字的函式內區域變數。靜態的函式內區域變數，會在程式第一次執行到宣告的程式碼時被初始化；其他擁有靜態儲存週期的物件，則會隨著程式一起被初始化。所有擁有靜態儲存週期的物件都會在程式結束時（可能會在未 join 的執行緒執行完成前發生）一併被摧毀。

    *動態* 初始化的意思是在初始化的過程中會發生一些比較不那麼單純的程序（例如：在建構式中會配置記憶體，或是某個變數初始化的過程中會以目前的行程 ID 做為參數）。另一種是靜態初始化。不過這兩者並不是完全相對的：靜態初始化 *一定* 會發生在擁有靜態儲存週期的物件上（初始為某個給定的常數，或是以內部資料全部為 0 的方式呈現），接下來，如果需要的話，就會發生動態初始化。

優點：

    全域/靜態變數在許多應用情境下都非常有用：具名常數、某些轉譯單元 (translation unit，經過前置處理器處理過的單一程式碼檔案) 內部的輔助資料結構、命令列的旗標、log 記錄、註冊機制 (registration mechanisms)、背景基礎服務 (background infrastructure)... 等等。

缺點：

    若是全域/靜態變數使用到動態初始化、或是 non-trivial 的解構式的話，情況就會變得複雜，容易產生非常難抓的 bug。動態初始化以及解構式的呼叫順序，在不同的轉譯單元間，並沒有一定的順序（不過物件的解構會以初始化的相反順序執行）。若是某項初始化程序會參考到另一個擁有靜態儲存週期的變數，那麼它有可能在物件的生命週期開始之前（或之後）存取該物件。另外，若是程式建立的執行緒在主程式結束後仍繼續執行，那麼那些執行緒就有可能會去存取已經被解構、生命週期已經結束的物件。

結論：

    **在解構方面**

        Trivia 解構式的執行順序並不重要（因為基本上它們什麼都沒做）；否則我們就有「在物件生命週期結束後仍去存取該物件」的風險。因此，只有 trivially destructible 的物件，才能擁有靜態儲存週期。基礎型別（像是指標和 ``int``）和陣列（組成型別必需為 trivially destructible），都算是 trivially destructible。另外，只要變數加上 ``constexpr``，就一定是 trivially destructible。

        .. code-block:: c++

            const int kNum = 10;  // 可以

            struct X { int n; };
            const X kX[] = {{1}, {2}, {3}};  // 可以

            void foo() {
              static const char* const kMessages[] = {"hello", "world"};  // 可以
            }

            // 可以：constexpr 確保一定是 trivially destructible
            constexpr std::array<int, 3> kArray = {{1, 2, 3}};

        .. rst-class:: bad-code
        .. code-block:: c++

            // 不好：解構式非 trivial
            const string kFoo = "foo";

            // 不好。理由同上，即使 kBar 是一個 reference。
            // （這項規則同樣適用於生命週期被延長的暫存物件）
            const string& kBar = StrCat("a", "b", "c");

            void bar() {
              // 不好：解構式非 trivial
              static std::map<int, int> kData = {{1, 0}, {2, 0}, {3, 0}};
            }

        請注意 reference 不是物件，因此它們沒有解構性質的限制。不過動態初始化的限制仍在。尤其是以 ``static T& t = *new T;`` 這樣的型式在函式內宣告的靜態區域 reference，是沒有問題的。

    **在初始化方面**

        初始化是個更加複雜的議題。這是因為我們需要考慮的不只是類別的建構式是否會執行，還要考慮初始值的計算過程與結果：

        .. code-block:: c++

            int n = 5;    // 沒問題
            int m = f();  // ? （視 f 而定）
            Foo x;        // ? （視 Foo::Foo 而定）
            Bar y = g();  // ? （視 g 以及 Bar::Bar 而定）

        除了第一行以外都有不確定初始化順序的問題。

        我們所要尋找的概念，以 C++ 標準術語來說，叫做「常數初始化 (constant initialization)」。意思是說用來初始化的運算式必須要是常數運算式 (constant expression)。如果物件在初始化時必須呼叫建構式，那麼該建構式也必須定義為 ``constexpr``：

        .. code-block:: c++

            struct Foo { constexpr Foo(int) {} };

            int n = 5;  // 沒問題，5 是常數運算式
            Foo x(2);   // 沒問題，2 是常數運算式，而且 Foo 的建構式也是 constexpr
            Foo a[] = { Foo(1), Foo(2), Foo(3) };  // 沒問題

        常數初始化在任何情況下都可被接受。擁有靜態儲存週期的變數在進行常數初始化時，需加上 ``constexpr`` 修飾字，或是（如果可能的話）加上 `ABSL_CONST_INIT <https://github.com/abseil/abseil-cpp/blob/03c1513538584f4a04d666be5eb469e3979febba/absl/base/attributes.h#L540>`__ 屬性。若是擁有靜態儲存週期的非區域變數沒有加上前述的標記，就應該認定該變數會進行動態初始化，在檢視時要格外小心。

        相對來說，下列的初始化都是有問題的：

        .. rst-class:: bad-code
        .. code-block:: c++

            // 以下是一些定義。
            time_t time(time_t*);      // 不是 constexpr！
            int f();                   // 不是 constexpr！
            struct Bar { Bar() {} };

            // 有問題的初始化用法
            time_t m = time(nullptr);  // 用來初始化的運算式不是常數運算式
            Foo y(f());                // 同上
            Bar b;                     // 選用的建構式 Bar::Bar() 沒有 constexpr 修飾

        請儘量不要對非區域變數進行動態初始化；在一般情況下是完全禁止的。然而，若是程式中沒有任何其他的初始化過程與該項初始化有依存關係的話，那麼我們允許這麼做。在這樣的限制下，該項初始化的先後順序並不重要。例如：

        .. code-block:: c++

            int p = getpid();  // 可以，只要沒有其他的靜態變數在初始化時
                                // 會用到 p 的值。

        允許對靜態區域變數進行動態初始化（而且其實很常見）。

    通用原則

        * 全域字串：如果你需要全域/靜態的字串常數，考慮使用單純的字元陣列，或是指向字面字串 (string literal) 第一個元素的 ``char`` 指標。字面字串本身就具有靜態儲存週期，而且通常來說夠用了。

        * Map、set，以及其他的動態容器：如果你需要靜態、固定不變的資料集合（例如：要有一個可以搜尋的 set，或是需要查表），你不能用標準函式庫中的動態容器類別宣告靜態變數，因為它們的解構式都不是 trivial 的。你可以考慮使用 trivial 型別的陣列，例如：「``int`` 陣列」的陣列（用來取代「從 ``int`` 對應到 ``int`` 的 map」），或是 ``pair`` （像是 ``int`` 和 ``const char*`` 組成的 ``pair``）的陣列。如果資料集合不大，線性搜尋 (linear search) 就夠用了（而且也很有效率，因為不需要配置額外的記憶體）。如果需要的話，可以讓資料依序排列，然後使用二元搜尋 (binary search) 演算法。如果你真的想用動態容器的話，考慮使用函式內的區域靜態指標（後詳述）。

        * 自定型別的靜態變數：如果你需要自定型別的靜態常數資料，該型別的解構式必須為 trivial，而且必須要有 ``constexpr`` 的建構式。

        * 如果以上都不符合你的需求，你可以建立一個動態物件，然後將它的指標連結到一個函式內的區域靜態指標變數，永遠不要刪除它：

          .. code-block:: c++

            static const auto* const impl = new T(args...);

          （如果初始化的過程很複雜的話，可以放到函式或 lambda 運算式中。）

thread_local 變數
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    宣告在函式作用域之外的 ``thread_local`` 變數必須以真正編譯時期就決定的常數初始化，而且必須加上 `ABSL_CONST_INIT <https://github.com/abseil/abseil-cpp/blob/master/absl/base/attributes.h>`__ 屬性。在定義 thread-local 的資料時，儘量利用「加上 ``thread_local`` 修飾字」這種方法。

定義：

    從 C++11 開始，變數可以加上 ``thread_local`` 修飾字：

    .. code-block:: c++

        thread_local Foo foo = ...;

    ``thread_local`` 變數實作上是許多物件的組合。在不同的執行緒中存取這個變數時，其實是去存取不同的物件。從許多角度來看，``thread_local`` 變數跟 :ref:`靜態儲存週期變數 <static-and-global-variables>` 很像。舉例來說，它們都可以在命名空間作用域宣告、可以在函式中宣告，也可以當作靜態類別資料成員宣告；但它們不能宣告為一般的類別資料成員。

    ``thread_local`` 變數的宣告方式跟靜態變數很像，不過 ``thread_local`` 變數必須在每個執行緒中分別初始化，而不是在程式開始時初始化一次。這意味著在函式內宣告的 ``thread_local`` 變數不會有問題，但在其他地方宣告的 ``thread_local`` 變數則會遇到和靜態變數一樣的「初始化順序」的問題（當然還會有 ``thread_local`` 變數獨有的問題）。

    ``thread_local`` 變數的實例 (instance) 在所屬的執行緒結束時就會被摧毀，因此它們跟靜態變數不同，不會遇到解構順序的問題。

優點：

    * Thread-local 的變數天生就不會有資料競爭 (race) 的問題（因為通常只會被單一執行緒存取），因此在撰寫平行運算的程式時，``thread_local`` 格外有用。

    * ``thread_local`` 是 C++ 標準中唯一一個建立 thread-local 資料的方法。

缺點：

    * 存取 ``thread_local`` 變數時，可能會同時執行數量無法預測與控制的程式碼。

    * ``thread_local`` 變數事實上等同於全域變數。除了它天生執行緒安全 (thread-safe) 外，其他全域變數的缺點它都有。

    * ``thread_local`` 變數所使用的記憶體空間會隨同時執行的執行緒數量成正比成長（在最差的狀況下），這對程式來說可能會是一大負擔。

    * 一般的類別資料成員不能被宣告為 ``thread_local``。

    * ``thread_local`` 的效率可能不如某些編譯器的內建函式 (intrinsic)。

結論：

    在函式內部使用  ``thread_local`` 變數不會有安全性的問題，所以使用上沒有限制。值得一提的是：你可以利用函式內部的 ``thread_local`` 模擬「類別作用域」或是「命名空間作用域」的 ``thread_local`` 變數。作法是定義一個會傳出 ``thread_local`` 變數 reference 的函式/靜態方法：

    .. code-block:: c++

        Foo& MyThreadLocalFoo() {
          hread_local Foo result = ComplicatedInitialization();
          return result;
        }

    在類別或命名空間作用域宣告的 ``thread_local`` 變數必須要以「真正編譯時期就決定的常數」初始化（也就是說不能有動態初始化行為）。為了確保這件事，在類別或命名空間作用域宣告的 ``thread_local`` 變數必須要加上 `ABSL_CONST_INIT <https://github.com/abseil/abseil-cpp/blob/master/absl/base/attributes.h>`__ 屬性（或是加上 ``constexpr``，但還是儘量用前面的方法）：

    .. code-block:: c++

        ABSL_CONST_INIT thread_local Foo foo = ...;

    在定義 thread-local 的變數時，儘量使用「加上 ``thread_local`` 修飾詞」這種方法，避免使用其他方法。