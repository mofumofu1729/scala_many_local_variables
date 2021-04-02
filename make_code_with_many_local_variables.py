#!/usr/bin/env python3
# coding: utf-8
import argparse


# 指定された個数のローカル変数の定義を含むScalaコードを生成

CODE_TEMPLATE = '''
object Main {{
  def main(args: Array[String]): Unit = {{
{0}

    println("hello world")
  }}
}}
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, required=True)
    parser.add_argument('--out', type=str, required=True)
    args = parser.parse_args()

    definitions_str = ''
    for i in range(args.n):
        definitions_str += "    val a{}: Int = 0\n".format(i+1)

    code = CODE_TEMPLATE.format(definitions_str)

    with open(args.out, mode='w') as f:
        f.write(code)


if __name__ == "__main__":
    main()
