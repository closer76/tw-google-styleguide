格式
------------

程式碼風格和格式確實比較隨意，但在一個專案中，若是所有人都使用相同的風格，那麼合作起來會比較輕鬆。不一定每個人都能同意以下每一條格式規則，有些規則必需要花點時間才能適應，但所有專案的成員遵從這些規則是很重要的，只有這樣才能讓所有人能很輕鬆的閱讀和理解其他人所撰寫的程式碼。

我們建立了一份 `emacs 設定檔 <https://raw.githubusercontent.com/google/styleguide/gh-pages/google-c-style.el>`_ 來幫助你撰寫符合正確格式的程式碼。

.. _line-length:

每行長度
~~~~~~~~~~~~~~~~~~~~

.. tip::

    每一行程式碼的長度最多不超過 80 個字元。

我們也了解這條規則是有爭議的，但很多現有程式碼都已經遵守這一項規則，我們覺得一致性更重要。

優點：

    提倡該原則的人主張強迫他們調整編輯器視窗大小非常無禮。有些人習慣同時並排開幾個程式碼視窗，根本沒有多餘空間把視窗拉大。大家都假設視窗不會超過某個大小來調整自己的工作環境，而且 80 欄寬是傳統標準。為什麼要改呢？

缺點：

    反對該原則的人則認為更大的欄寬讓程式碼更容易閱讀。80 欄的限制是上個世紀 60 年代大型主機的陳腐缺陷；現代設備具有更寬的螢幕，可以很輕鬆地顯示更多程式碼。

結論：

    80 個字元是每行的上限。

    但在下列情況下可以有彈性地超過這個限制：

        - 如果該行是註解，且為了不妨礙閱讀、方便複製貼上、或為了能自動連結等原因而不方便切斷者。例如：命令列指令的範例、超過 80 個字元的 URL 等。
        - 如果該行是 include 陳述式。
        - 如果該行為 :ref:`#define 保護 <define-guard>`。
        - 如果該行為 using 宣告。

.. _non-ascii-characters:

非 ASCII 字元
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    儘量不使用非 ASCII 字元，使用時必須使用 UTF-8 編碼。

即使是英文，也不應將軟體使用者會看到的文字寫死在程式碼中，因此應儘量避免使用非 ASCII 字元。不過，在特殊情況下可以適當包含此類字元。例如，如果你的程式碼需要解析來自非英語系國家的資料檔案，可以適當將其中當成分隔符號使用的非 ASCII 字串寫死在程式碼中；更常見的是（不需要本地化的）單元測試程式碼可能包含非 ASCII 字串。遇到這些狀況時，非 ASCII 字元應使用 UTF-8 編碼，因為很多工具都可以理解和處理 UTF-8 編碼。

十六進制編碼也可以，若是能增強可讀性的話更是鼓勵這麼做 —— 例如 ``"\xEF\xBB\xBF"``\ （或是更簡潔的寫法：``u8"\uFEFF"`` 在 Unicode 中是「零寬度、無間斷」的空格符號，如果不用十六進制格式直接放在 UTF-8 編碼的原始碼中，是看不到的。

用 ``u8`` 前綴以確保帶有 ``\uXXXX`` 跳脫序列的字面字串會以 UTF-8 格式編碼。不要在本身就帶有 UTF-8 編碼的非 ASCII 字元的字串前面加上 ``u8``，因為如果編譯器不把原始碼檔案當成 UTF-8 編碼來處理，輸出的結果就會是錯的。

不要使用用 C++11 的 ``char16_t`` 和 ``char32_t``，因為它們是給非 UTF-8 編碼的文字用的。同理，也不要使用 ``wchar_t``\ （除非你寫的程式碼要呼叫廣泛使用 ``wchar_t`` 的 Windows API）。

.. _spaces-vs-tabs:

該用空格還是 Tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    只使用空格，縮排時每次使用 2 個空格。

我們使用空格縮排。不要在程式碼中使用 tab。你應該調整設定，讓編輯器在你按下 tab 鍵時插入空格。

.. _function-declarations-and-definitions:

函式宣告與定義
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    回傳型別和函式名稱放在同一行。如果放得下的話，參數也儘量放在同一行。放不下的話，參數列就依 :ref:`函式呼叫 <function-calls>` 的方式分行。

函式看上去像這樣：

.. code-block:: c++

    ReturnType ClassName::FunctionName(Type par_name1, Type par_name2) {
      DoSomething();
      ...
    }

如果同一行文字太多，放不下所有參數：

.. code-block:: c++

    ReturnType ClassName::ReallyLongFunctionName(Type par_name1, Type par_name2,
                                                 Type par_name3) {
      DoSomething();
      ...
    }

甚至連第一個參數都放不下：

.. code-block:: c++

    ReturnType LongClassName::ReallyReallyReallyLongFunctionName(
        Type par_name1,  // 4 空格縮排
        Type par_name2,
        Type par_name3) {
      DoSomething();  // 2 空格縮排
      ...
    }

注意以下幾點：

    - 幫參數取適合的名稱。

    - 只有在參數在函式定義中沒有被使用到的情況下，才可以省略參數的名稱。

    - 如果回傳型別和函式名稱一行放不下，將兩者分行放。

    - 如果回傳型別與函式宣告或定義分行了，不要縮排。

    - 左括號一定要和函式名稱在同一行。

    - 函式名稱和左括號間不得有空格。

    - 括號與參數間不得有空格。

    - 左大括號一定要放在函式宣告最後一行的行尾，不要放在換行後的開頭。

    - 右大括號總是單獨位於函式最後一行，或者與左大括號同一行。

    - 右括號和左大括號之間要有一個空格。

    - 所有參數應儘可能對齊。

    - 縮排預設為 2 個空格。

    - 換行後的參數保持 4 個空格的縮排。

沒有用到、而且看前後文就可以了解的參數，名稱可以省略：

.. code-block:: c++

    class Foo {
     public:
      Foo(Foo&&);
      Foo(const Foo&);
      Foo& operator=(Foo&&);
      Foo& operator=(const Foo&);
    };

若是沒有用到的參數，但不是那麼容易理解的話，在函式定義處將參數名註解起來：

.. code-block:: c++

    class Shape {
     public:
      virtual void Rotate(double radians) = 0;
    }

    class Circle : public Shape {
     public:
      void Rotate(double radians) override;
    }

    void Circle::Rotate(double /*radians*/) {}

.. rst-class:: bad-code
.. code-block:: c++

    // 不好 - 如果將來有人要實作，很難猜出變數是幹什麼用的。
    void Circle::Rotate(double) {}

屬性、以及會展開成屬性的巨集，要放在函式宣告或定義的最前面，比回傳型別更前面：

.. code-block:: c++

    MUST_USE_RESULT bool IsOK();

.. _formatting-lambda-expressions:

Lambda 運算式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    Lambda 運算式的參數和實作內容格式和一般函式相同；capture list 的格式則和其他以逗點分開的列表相同。

若是以 by-reference 方式 capture，變數名稱和 ``&`` 之間不留空格。

.. code-block:: c++

    int x = 0;
    auto x_plus_n = [&x](int n) -> int { return x + n; }

如果 lambda 夠短的話，可以直接將完整內容寫在行內，當成函式的引數。

.. code-block:: c++

    std::set<int> blacklist = {7, 8, 9};
    std::vector<int> digits = {3, 9, 1, 8, 4, 7, 1};
    digits.erase(std::remove_if(digits.begin(), digits.end(), [&blacklist](int i) {
                   return blacklist.find(i) != blacklist.end();
                 }),
                 digits.end());

.. _function-calls:

函式呼叫
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    你可以一行寫完函式呼叫，也可以將括號內的參數分行，或是將參數放到下一行並且加上 4 格的縮排。如果沒有其它顧慮的話，儘可能精簡行數，比如把多個參數適當地放在同一行裡。

函式呼叫為以下的形式：

.. code-block:: c++

    bool result = DoSomething(argument1, argument2, argument3);

如果同一行放不下，可斷為多行，後面每一行都和第一個引數對齊，左括號後和右括號前不要留空格：

.. code-block:: c++

    bool result = DoSomething(averyveryveryverylongargument1,
                              argument2, argument3);

參數也可以放在下一行，加上 4 格的縮排：

.. code-block:: c++

    if (...) {
      ...
      ...
      if (...) {
        bool result = DoSomething(
            argument1, argument2,  // 4 空格縮排
            argument3, argument4);
        ...
      }

儘量把多個參數放在同一行，以減少函式呼叫所需的行數，除非影響到可讀性。有人認為把每個參數都獨立成行，不僅更好讀，而且方便編輯參數。不過，比起容易編輯，我們更重視可讀性，且大部份可讀性的問題都可以使用下列各種技巧解決。

如果某些參數是略複雜的運算式，全部放在同一行會降低可讀性的話，那麼可以試著建立名稱較有意義的變數，暫存該運算式的結果，再傳入函式：

.. code-block:: c++

    int my_heuristic = scores[x] * y + bases[x];
    bool result = DoSomething(my_heuristic, x, y, z);

或是將比較難懂的引數單獨放在一行，再加上註解說明：

.. code-block:: c++

    bool retval = DoSomething(scores[x] * y + bases[x],  // Score heuristic.
                              x, y, z);

如果將每個參數獨立成行可讀性還是比較高的話，那就這麼做。要不要這麼做考量的原因還是該放在可讀性，而非其他的因素。

有時候引數照著某種結構排列對可讀性來說很重要。在這種狀況下，可以酌情按其結構來決定參數格式：

.. code-block:: c++

    // 通過 3x3 矩陣轉換 widget.
    my_widget.Transform(x1, x2, x3,
                        y1, y2, y3,
                        z1, z2, z3);

.. _braced-initializer-list-format:

``{}`` 初值列格式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    依照格式化函式呼叫的方式格式化 :ref:`braced_initializer_list`。

如果 ``{}`` 列跟在名稱（如型別或變數）後面出現，你可以把名稱當成函式的名稱、``{}`` 是函式呼叫的括號這樣的格式撰寫。如果沒有名稱的話，就當作有個長度為零的名稱。

.. code-block:: c++

    // 將 {} 初值列放在一行內的範例。
    return {foo, bar};
    functioncall({foo, bar});
    std::pair<int, int> p{foo, bar};

    // 若是你不得不斷行。
    SomeFunction(
        {"assume a zero-length name before {"},
        some_other_function_parameter);
    SomeType variable{
        some, other, values,
        {"assume a zero-length name before {"},
        SomeOtherType{
            "Very long string requiring the surrounding breaks.",
            some, other values},
        SomeOtherType{"Slightly shorter string",
                      some, other, values}};
    SomeType variable{
        "This is too long to fit all in one line"};
    MyType m = {  // 你也可以在 { 前斷行。
        superlongvariablename1,
        superlongvariablename2,
        {short, interior, list},
        {interiorwrappinglist,
         interiorwrappinglist2}};

.. _conditionals:

條件述句
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    括號內儘量不使用空格。關鍵字 ``if`` 和 ``else`` 不要放在同一行。

基本條件語句有兩種可以接受的格式。一種在括號和條件之間有空格，另一種沒有。

最常見的是沒有空格的格式。兩種格式其實都可以，重點是要 *保持一致性*。如果你是在修改既有的檔案，使用原有的格式。如果是建立新的程式碼，參考該目錄下或專案中其它檔案的格式。如果你還是不知道該怎麼做，而且也沒有個人偏好的話，就用沒有空格的格式。

.. code-block:: c++

    if (condition) {  // 括號裡沒空格。
      ...  // 2 空格縮排。
    } else if (...) {  // else 與 if 的右大括號放在同一行。
      ...
    } else {
      ...
    }

如果你比較喜歡在括號內部加空格：

.. code-block:: c++

    if ( condition ) {  // 括號內加上空格 - 較少用
      ...  // 2 空格縮排。
    } else {  // else 與 if 的右大括號放在同一行。
      ...
    }

注意在所有情況下，``if`` 和左括號間都有個空格。如果有大括號的話，右括號和左大括號之間也要有個空格：

.. rst-class:: bad-code
.. code-block:: c++

    if(condition)     // 差 - IF 後面沒空格。
    if (condition){   // 差 - { 前面沒空格。
    if(condition){    // 前面兩項錯誤犯好犯滿。

.. code-block:: c++

    if (condition) {  // 可 - IF 後面和 { 前面都留有適當的空格。

簡短的條件語句可以寫在同一行，如果這樣可讀性比較高的話。只有當句子簡單並且沒有使用 ``else`` 子句時可以使用：

.. code-block:: c++

    if (x == kFoo) return new Foo();
    if (x == kBar) return new Bar();

如果述句中有 ``else`` 的話就禁止如此使用：

.. rst-class:: bad-code
.. code-block:: c++

    // 不可以這樣子 - 當 ELSE 子句存在時，IF 陳述句卻只擠在同一行
    if (x) DoThis();
    else DoThat();

一般來說，單行語句不需要使用大括號，如果你喜歡用也沒問題；複雜的條件式或迴圈，使用大括號的話可讀性較佳。也有些專案要求 ``if`` 必須一定要跟著使用大括號：

.. code-block:: c++

    if (condition)
      DoSomething();  // 2 空格縮排。

    if (condition) {
      DoSomething();  // 2 空格縮排。
    }

但如果整個述句中某個 ``if``-``else`` 的區塊使用了大括號的話，其它區塊也必須使用：

.. rst-class:: bad-code
.. code-block:: c++

    // 不可以這樣子 - IF 有大括號 ELSE 卻沒有。
    if (condition) {
      foo;
    } else
      bar;

    // 不可以這樣子 - ELSE 有大括號 IF 卻沒有。
    if (condition)
      foo;
    else {
      bar;
    }


.. code-block:: c++

    // 只要其中一個區塊用了大括號，兩個區塊都要用。
    if (condition) {
      foo;
    } else {
      bar;
    }

.. _loops-and-switch-statements:

迴圈和 ``switch`` 述句
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    ``switch`` 述句內可以使用大括號分段。若不同的 ``case`` 之前要 fall-through 的話，必須明確註明。若是迴圈內的述句只有一行的話，大括號可以省略。空的迴圈本體應使用一組內部無程式碼的大括號，或是 ``continue``。

``switch`` 述句中的 ``case`` 區塊用不用大括號都可以，取決於你的個人喜好。如果要使用的話，請依照下文所述的格式使用。

如果不是使用列舉值當成 ``case`` 的條件，那麼 ``switch`` 就一定要有 ``default`` 區塊（如果是用列舉值的話，只要有沒有處理到的值，編譯器就會產生警告）。如果程式不應該跑到 ``default``，就把它當成錯誤狀態。例如：

.. code-block:: c++

    switch (var) {
      case 0: {  // 2 空格縮排
        ...      // 4 空格縮排
        break;
      }
      case 1: {
        ...
        break;
      }
      default: {
        assert(false);
      }
    }

要從某個 ``case`` 標籤 fall-through 到下一個的話，必須使用 ``ABSL_FALLTHROUGH_INTENDED;`` 巨集（定義在 ``absl/base/macros.h`` 中）明確標示。``ABSL_FALLTHROUGH_INTENDED;`` 應該要放在放在執行到「要 fall-through 到下一個 ``case`` 標籤」的地方。例外狀況是：若是有數個連續而又不帶任何程式碼的 ``case`` 標籤，就不需要特別註明。

.. code-block:: c++

    switch (x) {
      case 41:  // 此處不需特別註明。
      case 43:
        if (dont_be_picky) {
          // 使用下列的巨集取代、或額外加上說明用的註解。
          ABSL_FALLTHROUGH_INTENDED;
        } else {
          CloseButNoCigar();
          break;
        }
      case 42:
        DoSomethingSpecial();
        ABSL_FALLTHROUGH_INTENDED;
      default:
        DoSomethingGeneric();
        break;
    }

若迴圈中只有一行述句，加不加大括號都可以。

.. code-block:: c++

    for (int i = 0; i < kSomeNumber; ++i)
      printf("I love you\n");

    for (int i = 0; i < kSomeNumber; ++i) {
      printf("I take it back\n");
    }

空的迴圈本體應使用一組內部無程式碼的大括號，或是 ``continue``，而不要就放一個分號在那邊。

.. code-block:: c++

    while (condition) {
      // 反覆直到條件失效。
    }
    for (int i = 0; i < kSomeNumber; ++i) {}  // 可 - 寫在同一行也沒有問題。
    while (condition) continue;  // 可 - contunue 表明沒有邏輯運算。

.. rst-class:: bad-code
.. code-block:: c++

    while (condition);  // 不好 - 看起來像是 while/loop 的一部分。

.. _pointer-and-reference-expressions:

指標和 reference 運算式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    句點或箭頭前後不要有空格。指標運算子之後不能有空格。

下面是指標和 reference 運算式的正確使用範例：

.. code-block:: c++

    x = *p;
    p = &x;
    x = r.y;
    x = r->y;

請注意：

    - 在存取成員時，句點或箭頭前後沒有空格。
    - 指標運算子 ``*`` 或 ``&`` 後面沒有空格。

在宣告指標變數或參數時，星號要靠在型別還是變數名稱旁邊都可以：

.. code-block:: c++

    // 沒問題，空格放在星號前。
    char *c;
    const string &str;

    // 沒問題，空格放在星號後。
    char* c;
    const string& str;

在單一檔案內的風格要保持一致，所以如果是修改現有檔案，請遵守該檔案的風格。

我們允許（但不常用）在同一行宣告式中宣告 1 個以上的變數，但其中不得有指標或是 reference 的宣告，因為這樣的宣告式很容易造成混淆。

.. code-block:: c++

    // 如果對可讀性有幫助就沒問題。
    int x, y;

.. rst-class:: bad-code
.. code-block:: c++

    int x, *y;  // 禁止 - 多個變數的宣告式中不得有 & 或 *
    char * c;  // 不好 - 星號前後都有空格
    const string & str;  // 不好 - & 前後都有空格

.. _boolean-expressions:

布林 (Boolean) 運算式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    如果一個布林運算式超過 :ref:`標準行寬 <line-length>`，斷行的方式要保持一致。

下面的例子中，``&&`` 運算子一律位於行尾：

.. code-block:: c++

    if (this_one_thing > this_other_thing &&
        a_third_thing == a_fourth_thing &&
        yet_another & last_one) {
      ...
    }

請注意在上述的例子中，兩個 ``&&`` 運算子均位於行尾。這樣的格式在 Google 的程式碼中很常見，雖然你要把所有運算子放在開頭也可以。可以額外加上括號，合理使用的話對增加可讀性是很有幫助的。此外，請直接用符號形式的運算子，例如 ``&&`` 和 ``~``，而不要用單字形式的運算子，如 ``and`` 和 ``compl``。

.. _return-values:

函式回傳值
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    除非必要，``return`` 運算式中不用加括號。

若是你寫 ``x = epr`` 中的 ``expr`` 時會加上括號，那 ``return expr;`` 中的 ``expr`` 才需要括號。

.. code-block:: c++

    return result;                  // 返回值很簡單，不需要括號。
    // 把複雜的運算式包起來，改善可讀性。這時使用括號就 OK。
    return (some_long_condition &&
            another_condition);

.. rst-class:: bad-code
.. code-block:: c++

    return (value);                // 你不會寫 var = (value);
    return(result);                // return 不是一個函式！

.. _variable-and-array-initialization:

變數及陣列初始化
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    用 ``=``、``()`` 或 ``{}`` 均可。

你可以用 ``=``、``()`` 或 ``{}``，以下用法都對：

.. code-block:: c++

    int x = 3;
    int x(3);
    int x{3};
    string name("Some Name");
    string name = "Some Name";
    string name{"Some Name"};

若是某型別有 ``std::initializer_list`` 建構式的話，使用 ``{}`` 初始列要特別小心。一個「不是空的」``{}`` 初始列會優先喚起 ``std::initializer_list`` 建構式。注意「空的」``{}`` 初始列是個例為，它會喚起預設建構式。若是想要呼叫「非 ``std::initializer_list``」的建構式，請改用括號進行初始化。

.. code-block:: c++

    std::vector<int> v(100, 1);  // vector 中有 100 個元素：每個元素都是 1
    std::vector<int> v{100, 1};  // vector 中有 2 個元素：100 和 1

此外，``{}`` 初始列不允許整數型別的縮小 (narrowing) 轉換，這可以用來避免一些型別上的程式撰寫錯誤。

.. code-block:: c++

    int pi(3.14);  // 可 -- pi == 3.
    int pi{3.14};  // 編譯器錯誤：縮小轉換

.. _preprocessor-directives:

前置處理器 (Preprocessor) 指令
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    以井號 ``#`` 開頭的前置處理器指令一律從一行的最開頭寫起。

即使前置處理器指令位於縮排程式碼區塊中，也應該最開頭寫起。

.. code-block:: c++

    // 可 - 指令從行首寫起
      if (lopsided_score) {
    #if DISASTER_PENDING      // 正確 -- 從行首寫起。
        DropEverything();
    # if NOTIFY               // 可以，但非必要 -- # 後面有空格
        NotifyClient();
    # endif
    #endif
        BackToNormal();
      }

.. rst-class:: bad-code
.. code-block:: c++

    // 不可 - 讓指令縮排
      if (lopsided_score) {
        #if DISASTER_PENDING  // 錯了！ "#if" 應該放在行開頭
        DropEverything();
        #endif                // 錯了！ "#endif" 不要縮排
        BackToNormal();
      }

.. _class-format:

類別格式
~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    存取控制區塊的宣告依次序是 ``public:``、``protected:``、``private:``，每次縮排 1 個空格。

類別宣告（這裡不談註解；想了解類別的註解原則，請參考 :ref:`class-comments`）的基本格式如下：

.. code-block:: c++

    class MyClass : public OtherClass {
     public:      // 注意有 1 空格縮排！
      MyClass();  // 一般的 2 空格縮排。
      explicit MyClass(int var);
      ~MyClass() {}

      void SomeFunction();
      void SomeFunctionThatDoesNothing() {
      }

      void set_some_var(int var) { some_var_ = var; }
      int some_var() const { return some_var_; }

     private:
      bool SomeInternalFunction();

      int some_var_;
      int some_other_var_;
    };

注意事項：

    - 所有基礎類別名稱應在 80 個字元的限制下儘量與子類別名稱放在同一行。

    - 關鍵詞 ``public:``、``protected:`` 和 ``private:`` 要縮排 1 個空格。

    - 除第一個關鍵詞外，其他關鍵詞前要空一行。如果類別較小的話也可以不空。

    - 這些關鍵詞後不要保留空行。

    - ``public`` 放在最前面，然後是 ``protected``，最後是 ``private``。

    - 關於宣告順序的規則請參考 :ref:`declaration-order` 一節。

.. _constructor-initializer-list:

建構式初值列 (Initializer List)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    建構式初值列可以放在同一行，或換行後縮排 4 個空格。

建構式初值列可接受的格式如下：

.. code-block:: c++

    // 當一行可以塞得下時：
    MyClass::MyClass(int var) : some_var_(var) {
      DoSomething();
    }

    // 如果一行塞不下建構式名稱列和初值列的話，你必須
    // 在分號前換行，並且縮排 4 個空格
    MyClass::MyClass(int var)
        : some_var_(var), some_other_var_(var + 1) {
      DoSomething();
    }

    // 若是初值列得分成好幾行的話，每個成員各占一行，
    // 排列整齊：
    MyClass::MyClass(int var)
        : some_var_(var),             // 4 格縮排
          some_other_var_(var + 1) {  // 對齊前一行
      DoSomething();
    }

    // 和其他程式碼區塊一樣，如果塞得下的話，右大括號可以
    // 和左大括號放在同一行。
    MyClass::MyClass(int var)
        : some_var_(var) {}

.. _namespace-formatting:

命名空間格式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    命名空間的內容不縮排。

:ref:`命名空間 <namespaces>` 不要增加額外的縮排層次，例如：

.. code-block:: c++

    namespace {

    void foo() {  // 正確。命名空間內沒有額外的縮排。
      ...
    }

    }  // namespace

命名空間的內容不要縮排：

.. rst-class:: bad-code
.. code-block:: c++

    namespace {

      // 錯！縮排多餘了。
      void foo() {
        ...
      }

    }  // namespace

宣告巢狀的命名空間時，每個命名空間都獨立成行。

.. code-block:: c++

    namespace foo {
    namespace bar {

水平空白
~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    依所在位置適當使用水平空白。絕對不要在行尾留下任何空白字元。

一般規則：

    .. code-block:: c++

        void f(bool b) {  // 左大括號前務必加上空格。
          ...
        int i = 0;  // 分號前通常不加空格。
        // {} 初始列中空格加不加都可以，不過兩邊必須一致！
        int x[] = { 0 };
        int x[] = {0};
        // 繼承與初值列中的冒號前後務必加上空格。
        class Foo : public Bar {
         public:
          // 至於 inline 函式實作，在大括號和實作內容間加上空格。
          Foo(int b) : Bar(), baz_(b) {}  // 空的大括號內不加空格。
          void Reset() { baz_ = 0; }  // 大括號和實作內容間用空格分開。
          ...

    在行尾添加空白字元會造成其他人在合併時的困擾，因為可能會把現有的空白字元刪掉。因此，行尾不要留下空白字元。如果你正在修改那一行，請順手刪除多餘的行尾空白字元，或是特別安排清理的工作（但最好確認目前沒有人還在修改這個檔案）。

迴圈和條件述句：

    .. code-block:: c++

        if (b) {          // 迴圈和條件句關鍵字後均有空格。
        } else {          // else 前後有空格。
        }
        while (test) {}   // 括號內部通常不緊鄰空格。
        switch (i) {
        for (int i = 0; i < 5; ++i) {
        // 循環和條件述句的括號內可以加上前後的空格。
        // ，但這樣的作法不常見。總之要一致。
        switch ( i ) {
        if ( test ) {
        for ( int i = 0; i < 5; ++i ) {
        // 迴圈中，分號後一定要有空格。分號前也可以
        // 加個空格，但不常見。
        for ( ; i < 5 ; ++i) {
          ...
        // Range-based for 迴圈中，冒號的前後必須各加一個空格。
        for (auto x : counts) {
          ...
        }
        switch (i) {
          case 1:         // switch case 的冒號前無空格。
            ...
          case 2: break;  // 如果冒號後有程式碼，在冒號後加個空格。

運算子：

    .. code-block:: c++

        // Assignment 運算子前後務必留空格。
        x = 0;

        // 其它二元運算子前也都要有空格，但乘號和除號前後也可以不加空格。
        // 括號內部前後不加空格。
        v = w * x + y / z;
        v = w*x + y/z;
        v = w * (x + z);

        // 在一元運算子和其參數之間不加空格。
        x = -5;
        ++x;
        if (x && !y)
          ...

模板和轉型：

    .. code-block:: c++

        // 尖括號（< 和 >）內部前後、< 前，以及轉型運算子的 > 和 ( 之間，都不要加空格。
        std::vector<string> x;
        y = static_cast<char*>(x);

        // 在類別與指標運算子之間可以留空格，但到底要不要須保持一致。
        std::vector<char *> x;

垂直空白/空行
~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    垂直空白/空行越少越好。

這不僅僅是規則而是原則問題了：除非必要，不要使用空行。尤其是：兩個函式定義之間的空行不要超過 2 行，函式起始處不要是空行，最後一行也不要是空行，其餘地方也儘量少用空行。在一個程式碼區塊中，空行像是文章中的段落：在視覺上將兩個想法區隔開來。

基本原則是：同一畫面可以顯示的程式碼越多，越容易追踪、理解程式的控制流程。當你需要刻意打斷這個流程時再加入空行。

空行使用時機的一些準則：

* 函式內開頭或結尾的空行對可讀性沒有幫助。
* 在多重 if-else 區塊裡加空行對可讀性可能有些幫助。
* 在註解前面加空行通常可以增加可讀性 — 引入一段新的註解等於在介紹一個新想法的開始，此時加上空行可以清楚地表示這段註解是在說明接下來的程式碼，而非延續前面的行為。
