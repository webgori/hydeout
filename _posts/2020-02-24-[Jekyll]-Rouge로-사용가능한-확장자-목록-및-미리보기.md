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
 * abap: SAP - Advanced Business Application Programming
 
 ``` abap
 lo_obj ?= lo_obj->do_nothing( 'Char' && ` String` ).
 
 SELECT SINGLE * FROM mara INTO ls_mara WHERE matkl EQ '1324'.
 LOOP AT lt_mara ASSIGNING <mara>.
   CHECK <mara>-mtart EQ '0001'.
 ENDLOOP.
 ```
 
 * actionscript: ActionScript [aliases: as,as3]
 * apache: configuration files for Apache web server
 * apiblueprint: Markdown based API description language. [aliases: apiblueprint,apib]
 * applescript: The AppleScript scripting language by Apple Inc. (http://developer.apple.com/applescript/) [aliases: applescript]
 * awk: pattern-directed scanning and processing language
 * biml: BIML, Business Intelligence Markup Language
 * brainfuck: The Brainfuck programming language
 * bsl: The 1C:Enterprise programming language
 * c: The C programming language
 
 ``` c
 #include "ruby/ruby.h"
 
 static int
 clone_method_i(st_data_t key, st_data_t value, st_data_t data)
 {
     clone_method((VALUE)data, (ID)key, (const rb_method_entry_t *)value);
     return ST_CONTINUE;
 }
 ```
 
 * ceylon: Say more, more clearly.
 * cfscript: CFScript, the CFML scripting language [aliases: cfc]
 * clojure: The Clojure programming language (clojure.org) [aliases: clj,cljs]
 * cmake: The cross-platform, open-source build system
 * coffeescript: The Coffeescript programming language (coffeescript.org) [aliases: coffee,coffee-script]
 * common_lisp: The Common Lisp variant of Lisp (common-lisp.net) [aliases: cl,common-lisp,elisp,emacs-lisp]
 * conf: A generic lexer for configuration files [aliases: config,configuration]
 * console: A generic lexer for shell sessions. Accepts ?lang and ?output lexer options, a ?prompt option, and ?comments to enable # comments. [aliases: terminal,shell_session,shell-session]
 
 ``` console
 # prints "hello, world" to the screen
 ~# echo Hello, World
 Hello, World
 
 # don't run this
 ~# rm -rf --no-preserve-root /
 ```
 
 * coq: Coq (coq.inria.fr)
 * cpp: The C++ programming language [aliases: c++]
 
 ``` cpp
 #include<iostream>
 
 using namespace std;
 
 int main()
 {
     cout << "Hello World" << endl;
 }
 ```
 
 * crystal: Crystal The Programming Language (crystal-lang.org) [aliases: cr]
 * csharp: a multi-paradigm language targeting .NET [aliases: c#,cs]
 
 ``` csharp
 // reverse byte order (16-bit)
 public static UInt16 ReverseBytes(UInt16 value)
 {
   return (UInt16)((value & 0xFFU) << 8 | (value & 0xFF00U) >> 8);
 }
 ```
 
 * css: Cascading Style Sheets, used to style web pages
 * d: The D programming language(dlang.org) [aliases: dlang]
 * dart: The Dart programming language (dartlang.com)
 * diff: Lexes unified diffs or patches [aliases: patch,udiff]
 * digdag: A simple, open source, multi-cloud workflow engine (https://www.digdag.io/)
 * docker: Dockerfile syntax [aliases: dockerfile]
 * dot: graph description language
 * eiffel: Eiffel programming language
 * elixir: Elixir language (elixir-lang.org) [aliases: elixir,exs]
 * elm: The Elm programming language (http://elm-lang.org/)
 * erb: Embedded ruby template files [aliases: eruby,rhtml]
 * erlang: The Erlang programming language (erlang.org) [aliases: erl]
 * escape: A generic lexer for including escaped content - see Formatter.enable_escape! [aliases: esc]
 * factor: Factor, the practical stack language (factorcode.org)
 * fortran: Fortran 2008 (free-form)
 * fsharp: F# (fsharp.net)
 * gherkin: A business-readable spec DSL ( github.com/cucumber/cucumber/wiki/Gherkin ) [aliases: cucumber,behat]
 * glsl: The GLSL shader language
 * go: The Go programming language (http://golang.org) [aliases: go,golang]
 
 ``` go
 package main
 
 import "fmt"
 
 func main() {
 	fmt.Println("Hello, 世界")
 }
 ```
 
 * gradle: A powerful build system for the JVM
 * graphql: GraphQL
 * groovy: The Groovy programming language (http://www.groovy-lang.org/)
 * hack: The Hack programming language (hacklang.org) [aliases: hack,hh]
 * haml: The Haml templating system for Ruby (haml.info) [aliases: HAML]
 * handlebars: the Handlebars and Mustache templating languages [aliases: hbs,mustache]
 * haskell: The Haskell programming language (haskell.org) [aliases: hs]
 * hcl: Hashicorp Configuration Language, used by Terraform and other Hashicorp tools
 * html: HTML, the markup language of the web
 * http: http requests and responses
 * hylang: The HyLang programming language (hylang.org) [aliases: hy]
 * idlang: Interactive Data Language
 * igorpro: WaveMetrics Igor Pro
 * ini: the INI configuration format
 * io: The IO programming language (http://iolanguage.com)
 * irb: Shell sessions in IRB or Pry [aliases: pry]
 * java: The Java programming language (java.com)
 
 ``` java
 public class java {
     public static void main(String[] args) {
         System.out.println("Hello World");
     }
 }
 ```
 
 * javascript: JavaScript, the browser scripting language [aliases: js]
 * jinja: Django/Jinja template engine (jinja.pocoo.org) [aliases: django]
 * json: JavaScript Object Notation (json.org)
 * json-doc: JavaScript Object Notation with extenstions for documentation
 * jsonnet: An elegant, formally-specified config language for JSON
 * jsp: JSP
 * jsx: React JSX (https://facebook.github.io/react/) [aliases: jsx,react]
 * julia: The Julia programming language [aliases: jl]
 * kotlin: Kotlin Programming Language (http://kotlinlang.org)
 
 ``` kotlin
 fun main(args: Array<String>) {
     println("Hello, world!")
 }
 ```
 
 * lasso: The Lasso programming language (lassosoft.com) [aliases: lassoscript]
 * liquid: Liquid is a templating engine for Ruby (liquidmarkup.org)
 * literate_coffeescript: Literate coffeescript [aliases: litcoffee]
 * literate_haskell: Literate haskell [aliases: lithaskell,lhaskell,lhs]
 * llvm: The LLVM Compiler Infrastructure (http://llvm.org/)
 * lua: Lua (http://www.lua.org)
 * m68k: Motorola 68k Assembler
 * magik: Smallworld Magik
 * make: Makefile syntax [aliases: makefile,mf,gnumake,bsdmake]
 * markdown: Markdown, a light-weight markup language for authors [aliases: md,mkd]
 * mathematica: Wolfram Mathematica, the world's definitive system for modern technical computing. [aliases: wl]
 * matlab: Matlab [aliases: m]
 * moonscript: Moonscript (http://www.moonscript.org) [aliases: moon]
 * mosel: An optimization language used by Fico's Xpress.
 * mxml: MXML
 * nasm: Netwide Assembler
 * nginx: configuration files for the nginx web server (nginx.org)
 * nim: The Nim programming language (http://nim-lang.org/) [aliases: nimrod]
 * nix: The Nix expression language (https://nixos.org/nix/manual/#ch-expression-language) [aliases: nixos]
 * objective_c: an extension of C commonly used to write Apple software [aliases: objc,obj-c,obj_c,objectivec]
 * ocaml: Objective Caml (ocaml.org)
 * pascal: a procedural programming language commonly used as a teaching language.
 
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
 
 * perl: The Perl scripting language (perl.org) [aliases: pl]
 
 ``` perl
 #!/usr/bin/env perl
 use warnings;
 print "a: ";
 my $a = "foo";
 print $a;
 ```
 
 * php: The PHP scripting language (php.net) [aliases: php,php3,php4,php5]
 
 ``` php
 <?php
   print("Hello {$world}");
 ?>
 ```
 
 * plaintext: A boring lexer that doesn't highlight anything [aliases: text]
 
 ``` plaintext
 plain text :)
 ```
 
 * plist: plist [aliases: plist]
 
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
 
 * powershell: powershell [aliases: posh,microsoftshell,msshell]
 
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
 
 * praat: The Praat scripting language (praat.org)
 * prolog: The Prolog programming language (http://en.wikipedia.org/wiki/Prolog) [aliases: prolog]
 * prometheus: prometheus [aliases: prometheus]
 
 ``` prometheus
 "this is a string"
 'these are unescaped: \n \\ \t'
 `these are not unescaped: \n ' " \t`
 
 http_requests_total{environment=~"staging|testing|development", method!="GET"}
 
 http_requests_total offset 5m
 
 sum(http_requests_total{method="GET"}[10m] offset 5m)
 ```
 
 * properties: .properties config files for Java
 
 ``` properties
 # You are reading the ".properties" entry.
 ! The exclamation mark can also mark text as comments.
 website = http\://en.wikipedia.org/
 language = English
 country : Poland
 continent=Europe
 key.with.dots=This is the value that could be looked up with the key "key.with.dots".
 ```
 
 * protobuf: Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data [aliases: proto]
 * puppet: The Puppet configuration management language (puppetlabs.org) [aliases: pp]
 * python: The Python programming language (python.org) [aliases: py]
 
 ``` python
 def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print a,
         a, b = b, a+b
 ```
 
 * q: The Q programming language (kx.com) [aliases: kdb+]
 * qml: QML, a UI markup language [aliases: qml]
 * r: The R statistics language (r-project.org) [aliases: r,R,s,S]
 * racket: Racket is a Lisp descended from Scheme (racket-lang.org)
 * ruby: The Ruby programming language (ruby-lang.org) [aliases: rb]
 
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
 
 * rust: The Rust programming language (rust-lang.org) [aliases: rs,rust,no_run,rs,no_run,rust,ignore,rs,ignore,rust,should_panic,rs,should_panic]
 * sass: The Sass stylesheet language language (sass-lang.com)
 
 ``` sass
 @for $i from 1 through 3
   .item-#{$i}
     width: 2em * $i
 ```
 
 * scala: The Scala programming language (scala-lang.org) [aliases: scala]
 
 ``` scala
 class Greeter(name: String = "World") {
   def sayHi() { println("Hi " + name + "!") }
 }
 ```
 
 * scheme: The Scheme variant of Lisp
 * scss: SCSS stylesheets (sass-lang.com)
 * sed: sed, the ultimate stream editor
 * shell: Various shell languages, including sh and bash [aliases: bash,zsh,ksh,sh]
 
 ``` shell
 # If not running interactively, don't do anything
 [[ -z "$PS1" ]] && return
 ```
 
 * sieve: mail filtering language
 * slim: The Slim template language
 * smalltalk: The Smalltalk programming language [aliases: st,squeak]
 * smarty: Smarty Template Engine [aliases: smarty]
 * sml: Standard ML [aliases: ml]
 * sqf: Status Quo Function, a Real Virtuality engine scripting language
 * sql: Structured Query Language, for relational databases
 
 ``` sql
 SELECT * FROM `users` WHERE `user`.`id` = 1
 ```
 
 * supercollider: A cross-platform interpreted programming language for sound synthesis, algorithmic composition, and realtime performance
 * swift: Multi paradigm, compiled programming language developed by Apple for iOS and OS X development. (developer.apple.com/swift)
 
 ``` swift
 // Say hello to poeple
 func sayHello(personName: String) -> String {
     let greeting = "Hello, " + personName + "!"
     return greeting
 }
 ```
 
 * tap: Test Anything Protocol [aliases: tap]
 * tcl: The Tool Command Language (tcl.tk)
 * terraform: Terraform HCL Interpolations [aliases: tf]
 * tex: The TeX typesetting system [aliases: TeX,LaTeX,latex]
 * toml: the TOML configuration format (https://github.com/mojombo/toml)
 * tsx: tsx
 * tulip: the tulip programming language (twitter.com/tuliplang) [aliases: tulip]
 * turtle: Terse RDF Triple Language, TriG
 * twig: Twig template engine (twig.sensiolabs.org)
 * typescript: TypeScript, a superset of JavaScript [aliases: ts]
 
 ``` typescript
 $(document).ready(function() { alert('ready!'); });
 ```
 
 * vala: A programming language similar to csharp.
 * vb: Visual Basic [aliases: visualbasic]
 
 ``` vb
 Private Sub Form_Load()
     ' Execute a simple message box that says "Hello, World!"
     MsgBox "Hello, World!"
 End Sub
 ```
 
 * verilog: The System Verilog hardware description language
 * vhdl: Very High Speed Integrated Circuit Hardware Description Language
 * viml: VimL, the scripting language for the Vim editor (vim.org) [aliases: vim,vimscript,ex]
 
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
 
 * vue: Vue.js single-file components [aliases: vuejs]
 
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
 
 * wollok: Wollok lang
 * xml: XML
 
 ``` xml
 <?xml version="1.0" encoding="utf-8"?>
 <xsl:template match="/"></xsl:template>
 ```
 
 * xojo: Xojo [aliases: realbasic]
 * yaml: Yaml Ain't Markup Language (yaml.org) [aliases: yml]
 
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