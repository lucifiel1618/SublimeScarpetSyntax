// SYNTAX TEST "Packages/Scarpet/scarpet.sublime-syntax"

_; _a; _i; _x; _y; _z; _trace;
// ^^ variable.language.anonymous
pi; euler; true; false; null; 0xFFFFFFFF; 0b00011011; 1.1663787e-5;
//  ^^^^^ constant.language.anonymous
//                            ^^^^^^^^^^ meta.number.integer.hexadecimal
//                                        ^^^^^^^^^^ meta.number.integer.binary
//                                                    ^^^^^^^^^^^^ meta.number.float.decimal

function_call(x, y, ...z);
// <- meta.function-call.identifier variable.function
//           ^^^^^^^^^^^^ meta.function-call.arguments

function_call_linebreak
// <- meta.function-call.identifier variable.function
   (x, y, ...z);
// ^^^^^^^^^^^^ meta.function-call.arguments

function_call_with_expressions_in_arguments
   (x1 = 1; x2 = 2; x = (x1+x2); y = 3; z = 4; x, y, ...z);
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.function-call.arguments.scarpet meta.group.scarpet


function_declaration(x, y, ...z) -> (
// <- entity.name.function meta.function.identifier
//                  ^^^^^^^^^^^^ meta.function.parameters.scarpet
//                   ^ meta.function.parameters
//                      ^ meta.function.parameters
//                         ^^^ keyword.operator.unpacking.mapping
//                            ^ meta.function.parameters
//                               ^^ keyword.declaration.function.arrow
//                                  ^ punctuation.section.block.begin meta.function meta.block
    ret = x+y+...z;
//  ^^^ variable.other
//      ^ keyword.operator.assignment
    print(str('Sum total: "%.2f"', ret));
//  ^^^^^ support.function.builtin
//             ^^^^^^^^^^^^^^^^ string.quoted.single
//                         ^^^^ constant.other.placeholder
    return  (ret);
//  ^^^^^^ support.function.builtin
);
// <- punctuation.section.block.end meta.function meta.block

function_declaration_linebreak
// <- entity.name.function meta.function.identifier
(x, y, ...z)
// <- meta.function.parameters
->
// <- keyword.declaration.function.arrow
(
// <- punctuation.section.block.begin meta.function meta.block
return(0)
);
// <- punctuation.section.block.end meta.block

map_identifier = {
//               ^ meta.mapping punctuation.section.mapping.begin
    'key_str' -> ['datum', 'list'],
//  ^^^^^^^^^ meta.mapping.key
//            ^^ punctuation.separator.key-value
//               ^^^^^^^^^^^^^^^^^ meta.mapping.value meta.sequence.list
    ['key', 'list'] -> 'datum_str',
//  ^^^^^^^^^^^^^^^ meta.mapping.key meta.sequence.list
    key_function_call(x, y) -> datum_function_call(x, y),
//  ^^^^^^^^^^^^^^^^^^^^^^^ meta.mapping.key variable.meta.function-call
//                             ^^^^^^^^^^^^^^^^^^^^^^^^^ meta.mapping.value meta.function-call
    key_function_call(x, y) -> datum_function_declaration(x, y) -> x+y,
//  ^^^^^^^^^^^^^^^^^^^^^^^ meta.mapping.key variable.meta.function-call
//                             ^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.mapping.value meta.function-call
    {'key'->'map'} -> {'datum' -> 'map'}
//                 ^^ punctuation.separator.key-value
};

map_identifier:item_get_key;
// <- meta.variable.identifier
//            ^ meta.variable.item-access keyword.operator.get
//             ^^^^^^^^^^^^ meta.variable.item-access
map_identifier
~   item_match_key;
// <- meta.variable.item-access keyword.operator.match
//  ^^^^^^^^^^^^^^ meta.variable.identifier

map_identifier
~   'item matching accepts regex expression [a-Z][0-9]*[^\(\]\{\\]+\s{1}\w{1-2}\b.*?';
//   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.mode.basic.regexp
//                                                     ^^^^^^^^^^^ meta.set.regexp

do_for_loop(n) -> (
    sum = 0;
    for(range(n),
        sum += _^2;
        if(sum >= 20,
            break();
            )
        )
    print(sum);

);

"double-quoted-string is illegal";
//<- invalid.illegal.not-a-str
octal_number_is_illegal = 0o1234567;
//                        ^^^^^^^^^ meta.number.integer.octal invalid.illegal.number
illegal,use , of ,comma,;
//     ^ invalid.illegal.stray
//          ^ invalid.illegal.stray
//               ^ invalid.illegal.stray
//                     ^ invalid.illegal.stray
illegal -> arrow_operator;
//      ^^ invalid.illegal.arrow.scarpet