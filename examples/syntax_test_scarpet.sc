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
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.function-call.arguments


function_declaration(x, y, ...z) -> (
// <- entity.name.function meta.function.identifier
//                  ^^^^^^^^^^^^ meta.function.parameters.scarpet
//                   ^ meta.function.parameters
//                      ^ meta.function.parameters
//                         ^^^ keyword.operator.unpacking.mapping
//                            ^ meta.function.parameters
//                               ^^ keyword.declaration.function.arrow
//                                  ^ meta.function meta.block punctuation.section.block.begin
    ret = x+y+...z;
//  ^^^ variable.other
//      ^ keyword.operator.assignment
    print(str('Sum total: "%.2f"', ret));
//  ^^^^^ keyword.other.print
//             ^^^^^^^^^^^^^^^^^ string.quoted.single
//                         ^^^^ constant.other.placeholder
    return  (ret);
//  ^^^^^^ keyword.control.flow.return
);
// <- meta.function meta.block punctuation.section.block.end

function_declaration_linebreak
// <- entity.name.function meta.function.identifier
(x, y, ...z)
// <- meta.function.parameters
->
// <- keyword.declaration.function.arrow
(
// <- meta.function meta.block punctuation.section.block.begin
return(0)
);
// <- meta.block punctuation.section.block.end

map_identifier = {
//               ^ meta.mapping punctuation.section.mapping.begin
    'key_str' -> ['datum', 'list'],
//  ^^^^^^^^^ meta.mapping.key
//            ^^ punctuation.separator.key-value
//               ^^^^^^^^^^^^^^^^^ meta.mapping.value meta.sequence.list
    ['key', 'list'] -> 'datum_str',
//  ^^^^^^^^^^^^^^^ meta.mapping.key meta.sequence.list
    key_function_call(x, y) -> datum_function_call(x, y),
//  ^^^^^^^^^^^^^^^^^^^^^^^ meta.mapping.key meta.function-call
//                             ^^^^^^^^^^^^^^^^^^^^^^^^^ meta.mapping.value meta.function-call
    key_function_call(x, y) -> datum_function_declaration(x, y) -> x+y,
//  ^^^^^^^^^^^^^^^^^^^^^^^ meta.mapping.key meta.function-call
//                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.mapping.value meta.function
    {'key'->'map'} -> {'datum' -> 'map'}
//                 ^^ punctuation.separator.key-value
};

map_identifier:item_get_key;
// <- meta.variable.identifier
//            ^ keyword.operator.get

map_identifier
~   item_match_key;
// <- keyword.operator.match
//  ^^^^^^^^^^^^^^ meta.variable.identifier

map_identifier
~   'item matching accepts regex expression [a-Z][0-9]*[^\(\]\{\\]+\s{1}\w{1-2}\b.*?';
//   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.mode.basic.regexp
//                                                     ^^^^^^^^^^^ meta.set.regexp

format('u formatted', 'ibc string' 'uri preview', 'eb are supported!');

decorators = format('^ubic tooltips', '?suggestion', '!message', '@url', '&copy to clipboard text');

fontcolors = format(
    'w white', 'y yellow', 'r red', 'c cyan', 'p purple', 'e green',
    'm magenta', 'l lime', 't light blue', 'f dark gray', 'g gray', 'd gold',
    'n brown', 'q turquoise', 'v navy blue', 'k black',
    '#00AAAA hexcolor');

fontstyles_avalible = format('b bold', 'i italic', 'u underline');
fontstyles_unavalible = format('s strikethrough', 'o obfuscated');

more_valid_formats = format('bbbi#ABABA1ssosrso message')
//                           ^^^^^^^^^^^^^^^^^^ constant.other.string-format
//                                              ^^^^^^^ region.redish.string-format
//                                              ^^^^^^^ markup.bold.string-format
//                                              ^^^^^^^ markup.italic.string-format
//                                              ^^^^^^^ markup.strikethrough.string-format
invalid_fontfmts = format(
    'tyai including non-existing formatting symbols "a"',
//   ^^^^ invalid.illegal.string-format
    '#AABAFI invalid_hexcode',
//   ^^^^^^^ invalid.illegal.string-format
    'b#A0A0Ai invalid_hexcode'
//   ^^^^^^^^ invalid.illegal.string-format
);

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