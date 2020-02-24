---
published: true
title: "[Jekyll] Rouge로 사용가능한 프로그래밍 언어 목록 및 미리보기"
categories:
  - WEB
date: 2020-02-24T10:30:00.000Z
tags:
  - Jekyll
---

## 1. 개요
 * [Rouge Github]는 루비로 만든 문법 강조기입니다. 100개 이상의 프로그래밍 언어를 지원하며 Jekyll 3 버전 이후부터는 문법 강조기가 [Rouge Github]로 통일 되었습니다.
 * 포스팅을 할 때 문법 강조 별칭을 자주 잊어버려 따로 정리하게 되었습니다.
 
## 2. 2020년 02월 현재 지원하는 언어들 (미리보기는 Rouge monokai.sublime Theme)
 1. abap: SAP - Advanced Business Application Programming
 
 ``` abap
 lo_obj ?= lo_obj->do_nothing( 'Char' && ` String` ).
 
 SELECT SINGLE * FROM mara INTO ls_mara WHERE matkl EQ '1324'.
 LOOP AT lt_mara ASSIGNING <mara>.
   CHECK <mara>-mtart EQ '0001'.
 ENDLOOP.
 ```
 
 2. actionscript: ActionScript [aliases: as,as3]
 3. apache: configuration files for Apache web server
 4. apiblueprint: Markdown based API description language. [aliases: apiblueprint,apib]
 5. applescript: The AppleScript scripting language by Apple Inc. (http://developer.apple.com/applescript/) [aliases: applescript]
 6. awk: pattern-directed scanning and processing language
 7. biml: BIML, Business Intelligence Markup Language
 8. brainfuck: The Brainfuck programming language
 9. bsl: The 1C:Enterprise programming language
 10. c: The C programming language
 
 ``` c
 #include "ruby/ruby.h"
 
 static int
 clone_method_i(st_data_t key, st_data_t value, st_data_t data)
 {
     clone_method((VALUE)data, (ID)key, (const rb_method_entry_t *)value);
     return ST_CONTINUE;
 }
 ```
 
 11. ceylon: Say more, more clearly.
 12. cfscript: CFScript, the CFML scripting language [aliases: cfc]
 13. clojure: The Clojure programming language (clojure.org) [aliases: clj,cljs]
 14. cmake: The cross-platform, open-source build system
 15. coffeescript: The Coffeescript programming language (coffeescript.org) [aliases: coffee,coffee-script]
 16. common_lisp: The Common Lisp variant of Lisp (common-lisp.net) [aliases: cl,common-lisp,elisp,emacs-lisp]
 17. conf: A generic lexer for configuration files [aliases: config,configuration]
 18. console: A generic lexer for shell sessions. Accepts ?lang and ?output lexer options, a ?prompt option, and ?comments to enable # comments. [aliases: terminal,shell_session,shell-session]
 
 ``` console
 # prints "hello, world" to the screen
 ~# echo Hello, World
 Hello, World
 
 # don't run this
 ~# rm -rf --no-preserve-root /
 ```
 
 19. coq: Coq (coq.inria.fr)
 20. cpp: The C++ programming language [aliases: c++]
 
 ``` cpp
 #include<iostream>
 
 using namespace std;
 
 int main()
 {
     cout << "Hello World" << endl;
 }
 ```
 
 21. crystal: Crystal The Programming Language (crystal-lang.org) [aliases: cr]
 22. csharp: a multi-paradigm language targeting .NET [aliases: c#,cs]
 
 ``` csharp
 // reverse byte order (16-bit)
 public static UInt16 ReverseBytes(UInt16 value)
 {
   return (UInt16)((value & 0xFFU) << 8 | (value & 0xFF00U) >> 8);
 }
 ```
 
 23. css: Cascading Style Sheets, used to style web pages
 24. d: The D programming language(dlang.org) [aliases: dlang]
 25. dart: The Dart programming language (dartlang.com)
 26. diff: Lexes unified diffs or patches [aliases: patch,udiff]
 27. digdag: A simple, open source, multi-cloud workflow engine (https://www.digdag.io/)
 28. docker: Dockerfile syntax [aliases: dockerfile]
 29. dot: graph description language
 30. eiffel: Eiffel programming language
 31. elixir: Elixir language (elixir-lang.org) [aliases: elixir,exs]
 32. elm: The Elm programming language (http://elm-lang.org/)
 33. erb: Embedded ruby template files [aliases: eruby,rhtml]
 34. erlang: The Erlang programming language (erlang.org) [aliases: erl]
 35. escape: A generic lexer for including escaped content - see Formatter.enable_escape! [aliases: esc]
 36. factor: Factor, the practical stack language (factorcode.org)
 37. fortran: Fortran 2008 (free-form)
 38. fsharp: F# (fsharp.net)
 39. gherkin: A business-readable spec DSL ( github.com/cucumber/cucumber/wiki/Gherkin ) [aliases: cucumber,behat]
 40. glsl: The GLSL shader language
 41. go: The Go programming language (http://golang.org) [aliases: go,golang]
 
 ``` go
 package main
 
 import "fmt"
 
 func main() {
 	fmt.Println("Hello, 世界")
 }
 ```
 
 42. gradle: A powerful build system for the JVM
 43. graphql: GraphQL
 44. groovy: The Groovy programming language (http://www.groovy-lang.org/)
 45. hack: The Hack programming language (hacklang.org) [aliases: hack,hh]
 46. haml: The Haml templating system for Ruby (haml.info) [aliases: HAML]
 47. handlebars: the Handlebars and Mustache templating languages [aliases: hbs,mustache]
 48. haskell: The Haskell programming language (haskell.org) [aliases: hs]
 49. hcl: Hashicorp Configuration Language, used by Terraform and other Hashicorp tools
 50. html: HTML, the markup language of the web
 51. http: http requests and responses
 52. hylang: The HyLang programming language (hylang.org) [aliases: hy]
 53. idlang: Interactive Data Language
 54. igorpro: WaveMetrics Igor Pro
 55. ini: the INI configuration format
 56. io: The IO programming language (http://iolanguage.com)
 57. irb: Shell sessions in IRB or Pry [aliases: pry]
 58. java: The Java programming language (java.com)
 
 ``` java
 public class java {
     public static void main(String[] args) {
         System.out.println("Hello World");
     }
 }
 ```
 
 59. javascript: JavaScript, the browser scripting language [aliases: js]
 60. jinja: Django/Jinja template engine (jinja.pocoo.org) [aliases: django]
 61. json: JavaScript Object Notation (json.org)
 62. json-doc: JavaScript Object Notation with extenstions for documentation
 63. jsonnet: An elegant, formally-specified config language for JSON
 64. jsp: JSP
 65. jsx: React JSX (https://facebook.github.io/react/) [aliases: jsx,react]
 66. julia: The Julia programming language [aliases: jl]
 67. kotlin: Kotlin Programming Language (http://kotlinlang.org)
 
 ``` kotlin
 fun main(args: Array<String>) {
     println("Hello, world!")
 }
 ```
 
 68. lasso: The Lasso programming language (lassosoft.com) [aliases: lassoscript]
 69. liquid: Liquid is a templating engine for Ruby (liquidmarkup.org)
 70. literate_coffeescript: Literate coffeescript [aliases: litcoffee]
 71. literate_haskell: Literate haskell [aliases: lithaskell,lhaskell,lhs]
 72. llvm: The LLVM Compiler Infrastructure (http://llvm.org/)
 73. lua: Lua (http://www.lua.org)
 74. m68k: Motorola 68k Assembler
 75. magik: Smallworld Magik
 76. make: Makefile syntax [aliases: makefile,mf,gnumake,bsdmake]
 77. markdown: Markdown, a light-weight markup language for authors [aliases: md,mkd]
 78. mathematica: Wolfram Mathematica, the world's definitive system for modern technical computing. [aliases: wl]
 79. matlab: Matlab [aliases: m]
 80. moonscript: Moonscript (http://www.moonscript.org) [aliases: moon]
 81. mosel: An optimization language used by Fico's Xpress.
 82. mxml: MXML
 83. nasm: Netwide Assembler
 84. nginx: configuration files for the nginx web server (nginx.org)
 85. nim: The Nim programming language (http://nim-lang.org/) [aliases: nimrod]
 86. nix: The Nix expression language (https://nixos.org/nix/manual/#ch-expression-language) [aliases: nixos]
 87. objective_c: an extension of C commonly used to write Apple software [aliases: objc,obj-c,obj_c,objectivec]
 88. ocaml: Objective Caml (ocaml.org)
 89. pascal: a procedural programming language commonly used as a teaching language.
 
 ``` pascal
 program FizzBuzz(output);
 var
   i: Integer;
 begin
   for i := 1 to 100 do
     if i mod 15 = 0 then
       WriteLn('FizzBuzz')
     else if i mod 3 = 0 then
       WriteLn('Fizz')
     else if i mod 5 = 0 then
       WriteLn('Buzz')
     else
       WriteLn(i)
 end.
 Save this
 ```
 
 90. perl: The Perl scripting language (perl.org) [aliases: pl]
 
 ``` perl
 #!/usr/bin/env perl
 use warnings;
 print "a: ";
 my $a = "foo";
 print $a;
 ```
 
 91. php: The PHP scripting language (php.net) [aliases: php,php3,php4,php5]
 
 ``` php
 <?php
   print("Hello {$world}");
 ?>
 ```
 
 92. plaintext: A boring lexer that doesn't highlight anything [aliases: text]
 
 ``` plaintext
 plain text :)
 ```
 
 93. plist: plist [aliases: plist]
 
 ``` plist
 // !$*UTF8*$!
 {
 	archiveVersion = 1;
 	classes = {
 	};
 	objectVersion = 46;
 	objects = {
 	/* ... */
 	};
 	rootObject = B3A67937542EC2041CBF1CA2 /* Project object */;
 }
 ```
 
 94. powershell: powershell [aliases: posh,microsoftshell,msshell]
 
 ``` powershell
 function Verb-Noun
 {
     <#
     .SYNOPSIS
     Tells you what it does
 
     .DESCRIPTION
     Tells you what it does with more detail.
     #>
     param ([string]$Name, [string]$Extension = "txt", [string]$foo="bar")
     $name = $name + "." + $extension
     $name
 }
 ```
 
 95. praat: The Praat scripting language (praat.org)
 96. prolog: The Prolog programming language (http://en.wikipedia.org/wiki/Prolog) [aliases: prolog]
 97. prometheus: prometheus [aliases: prometheus]
 
 ``` prometheus
 "this is a string"
 'these are unescaped: \n \\ \t'
 `these are not unescaped: \n ' " \t`
 
 http_requests_total{environment=~"staging|testing|development", method!="GET"}
 
 http_requests_total offset 5m
 
 sum(http_requests_total{method="GET"}[10m] offset 5m)
 ```
 
 98. properties: .properties config files for Java
 
 ``` properties
 # You are reading the ".properties" entry.
 ! The exclamation mark can also mark text as comments.
 website = http\://en.wikipedia.org/
 language = English
 country : Poland
 continent=Europe
 key.with.dots=This is the value that could be looked up with the key "key.with.dots".
 ```
 
 99. protobuf: Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data [aliases: proto]
 100. puppet: The Puppet configuration management language (puppetlabs.org) [aliases: pp]
 101. python: The Python programming language (python.org) [aliases: py]
 
 ``` python
 def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print a,
         a, b = b, a+b
 ```
 
 102. q: The Q programming language (kx.com) [aliases: kdb+]
 103. qml: QML, a UI markup language [aliases: qml]
 104. r: The R statistics language (r-project.org) [aliases: r,R,s,S]
 105. racket: Racket is a Lisp descended from Scheme (racket-lang.org)
 106. ruby: The Ruby programming language (ruby-lang.org) [aliases: rb]
 
 ``` ruby
 class Greeter
   def initialize(name="World")
     @name = name
   end
 
   def say_hi
     puts "Hi #{@name}!"
   end
 end
 ```
 
 107. rust: The Rust programming language (rust-lang.org) [aliases: rs,rust,no_run,rs,no_run,rust,ignore,rs,ignore,rust,should_panic,rs,should_panic]
 108. sass: The Sass stylesheet language language (sass-lang.com)
 
 ``` sass
 @for $i from 1 through 3
   .item-#{$i}
     width: 2em * $i
 ```
 
 109. scala: The Scala programming language (scala-lang.org) [aliases: scala]
 
 ``` scala
 class Greeter(name: String = "World") {
   def sayHi() { println("Hi " + name + "!") }
 }
 ```
 
 110. scheme: The Scheme variant of Lisp
 111. scss: SCSS stylesheets (sass-lang.com)
 112. sed: sed, the ultimate stream editor
 113. shell: Various shell languages, including sh and bash [aliases: bash,zsh,ksh,sh]
 
 ``` shell
 # If not running interactively, don't do anything
 [[ -z "$PS1" ]] && return
 ```
 
 114. sieve: mail filtering language
 115. slim: The Slim template language
 116. smalltalk: The Smalltalk programming language [aliases: st,squeak]
 117. smarty: Smarty Template Engine [aliases: smarty]
 118. sml: Standard ML [aliases: ml]
 119. sqf: Status Quo Function, a Real Virtuality engine scripting language
 120. sql: Structured Query Language, for relational databases
 
 ``` sql
 SELECT * FROM `users` WHERE `user`.`id` = 1
 ```
 
 121. supercollider: A cross-platform interpreted programming language for sound synthesis, algorithmic composition, and realtime performance
 122. swift: Multi paradigm, compiled programming language developed by Apple for iOS and OS X development. (developer.apple.com/swift)
 
 ``` swift
 // Say hello to poeple
 func sayHello(personName: String) -> String {
     let greeting = "Hello, " + personName + "!"
     return greeting
 }
 ```
 
 123. tap: Test Anything Protocol [aliases: tap]
 124. tcl: The Tool Command Language (tcl.tk)
 125. terraform: Terraform HCL Interpolations [aliases: tf]
 126. tex: The TeX typesetting system [aliases: TeX,LaTeX,latex]
 127. toml: the TOML configuration format (https://github.com/mojombo/toml)
 128. tsx: tsx
 129. tulip: the tulip programming language (twitter.com/tuliplang) [aliases: tulip]
 130. turtle: Terse RDF Triple Language, TriG
 131. twig: Twig template engine (twig.sensiolabs.org)
 132. typescript: TypeScript, a superset of JavaScript [aliases: ts]
 
 ``` typescript
 $(document).ready(function() { alert('ready!'); });
 ```
 
 133. vala: A programming language similar to csharp.
 134. vb: Visual Basic [aliases: visualbasic]
 
 ``` vb
 Private Sub Form_Load()
     ' Execute a simple message box that says "Hello, World!"
     MsgBox "Hello, World!"
 End Sub
 ```
 
 135. verilog: The System Verilog hardware description language
 136. vhdl: Very High Speed Integrated Circuit Hardware Description Language
 137. viml: VimL, the scripting language for the Vim editor (vim.org) [aliases: vim,vimscript,ex]
 
 ``` viml
 function! s:Make(dir, make, format, name) abort
   let cd = exists('*haslocaldir') && haslocaldir() ? 'lcd' : 'cd'
   let cwd = getcwd()
   let [mp, efm, cc] = [&l:mp, &l:efm, get(b:, 'current_compiler', '')]
   try
     execute cd fnameescape(dir)
     let [&l:mp, &l:efm, b:current_compiler] = [a:make, a:format, a:compiler]
     execute (exists(':Make') == 2 ? 'Make' : 'make')
   finally
     let [&l:mp, &l:efm, b:current_compiler] = [mp, efm, cc]
     if empty(cc) | unlet! b:current_compiler | endif
     execute cd fnameescape(cwd)
   endtry
 endfunction
 ```
 
 138. vue: Vue.js single-file components [aliases: vuejs]
 
 ``` vue
 <template>
   <div id="app">
     {{ message }}
   </div>
 </template>
 
 <script lang=coffee>
   app = new Vue
     el: '#app'
     data: { message: 'Hello Vue!' }
 </script>
 ```
 
 139. wollok: Wollok lang
 140. xml: XML
 
 ``` xml
 <?xml version="1.0" encoding="utf-8"?>
 <xsl:template match="/"></xsl:template>
 ```
 
 141. xojo: Xojo [aliases: realbasic]
 142. yaml: Yaml Ain't Markup Language (yaml.org) [aliases: yml]
 
 ``` yaml
 ---
 one: Mark McGwire
 two: Sammy Sosa
 three: Ken Griffey
 ```
 
 * 지원하는 프로그래밍 언어 목록 출처: [Rouge GitHub Wiki]
 * 예제 코드 출처: [Rouge]
 
[Rouge Github]: <https://github.com/rouge-ruby/rouge>
[Rouge GitHub Wiki]: <https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers>
[Rouge]: <http://rouge.jneen.net/>