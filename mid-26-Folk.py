{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM3AXW1KzorUPyejNFWtZGR",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/fokkubja/26-fok-coding68/blob/main/mid-26-Folk.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#19/12/68 สอบกลางภาค"
      ],
      "metadata": {
        "id": "fa7vzw2Wpah9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "name = input(\"การุณาใช่ใส่ชื่อเล่นของท่าน\")\n",
        "print('สวัสดีครับ',name,'พร้อมที่จะคำนวณแล้วใช่ไหมครับ')\n",
        "p = int(input(\"ใส่ค่าของ pressure\"))\n",
        "v = int(input(\"ใส่ค่าของ volume\"))\n",
        "if  p<=0:\n",
        "  print('หาค่าไม่ได้')\n",
        "if v<=0:\n",
        "  print('หาค่าไม่ได้')\n",
        "else :\n",
        "  print('จะคำนวณโดยใช้สูตร T = (pressure x volume)/(8.314 x 1) ครับ')\n",
        "  t = (p*v)/(8.314*1)\n",
        "  print('ค่าของ temperature คือ',t)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IeXG-P9Yphdl",
        "outputId": "e77d4cde-1920-4c58-81ef-37d3733138cc"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "การุณาใช่ใส่ชื่อเล่นของท่านfok\n",
            "สวัสดีครับ fok พร้อมที่จะคำนวณแล้วใช่ไหมครับ\n",
            "ใส่ค่าของ pressure-5\n",
            "ใส่ค่าของ volume-5\n",
            "หาค่าไม่ได้\n",
            "หาค่าไม่ได้\n"
          ]
        }
      ]
    }
  ]
}