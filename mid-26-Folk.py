{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNEGl4IURJjgzQP62cUms9D",
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
        "print ('จะคำนวณโดยใช้สูตร T = (pressure x volume)/(8.314 x 1) ครับ')\n",
        "t = (p*v)/(8.314*1)\n",
        "print('ค่าของ temperature คือ',t)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IeXG-P9Yphdl",
        "outputId": "94dc894f-1927-4426-a5b9-5b53ef5b5c94"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "การุณาใช่ใส่ชื่อเล่นของท่านfok\n",
            "สวัสดีครับ fok พร้อมที่จะคำนวณแล้วใช่ไหมครับ\n",
            "ใส่ค่าของ pressure30\n",
            "ใส่ค่าของ volume30\n",
            "จะคำนวณโดยใช้สูตร T = (pressure x volume)/(8.314 x 1) ครับ\n",
            "ค่าของ temperature คือ 108.2511426509502\n"
          ]
        }
      ]
    }
  ]
}