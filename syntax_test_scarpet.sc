// SYNTAX TEST "Packages/Scarpet/scarpet.sublime-syntax"

_; _x; _y; _z;
// ^^ variable.language.anonymous
pi; euler;
//  ^^^^^ constant.language.anonymous

function_call(x, y, ...z);
// <- meta.function-call.identifier variable.function
//           ^^^^^^^^^^^^ meta.function-call.arguments
//            ^ meta.function-call.arguments variable.other

function_call_linebreak
   (x, y, ...z);
// ^^^^^^^^^^^^ meta.function-call.arguments

function_call_linebreak_w_comments
// <- meta.function-call.identifier variable.function
   (x, y, ...z);
// ^^^^^^^^^^^^ meta.function-call.arguments

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
(x, y, ...z)
->
(
return(0)
);

function_declaration_linebreak_w_comments
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
//                             ^^^^^^^^^^^^^^^^^^^^^^^^^ meta.mapping.value meta.function-call
    {'key'->'map'} -> {'datum'->'map'}
//                 ^^ punctuation.separator.key-value
};

map_identifier:item_access_key;
// <- meta.variable.identifier
//            ^ meta.variable.item-access keyword.operator.get
//             ^^^^^^^^^^^^^^^ meta.variable.item-access
map_identifier
~   item_access_key;
// <- meta.variable.item-access keyword.operator.match
//  ^^^^^^^^^^^^^^^ meta.variable.identifier

"double-quoted-strings are illegal"
