"use strict";

let str = prompt("Введите строку");

let operation = prompt(`Выберите операцию:
                        1 - посчитать количество символов в строке
                        2 - извлечь указанную часть строки
                        3 - поменять местами первый и последний символ строки
                        4 - заменить указанное слово
                        5 - привести строку к нижнему регистру
                        6 - привести строку к верхнему регистру
                        7 - добавить к выброной букве строку "!!!"`);

switch (operation) {
    case "1":
        alert(str.length);
        break;
    case "2":
        let num1 = prompt("Введите начальный индекс");
        let num2 = prompt("Введите конечный индекс");
        alert(str.slice(num1, num2));
        break;
    case "3":
        let firstChar = str[0];
        let lastChar = str[str.length - 1];
        alert(lastChar + str.slice(1, -1) + firstChar);
        break;
    case "4":
        let oldWord = prompt("Введите слово, которое нужно заменить");
        let newWord = prompt("Введите новое слово");
        alert(str.replace(oldWord, newWord));
        break;
    case "5":
        alert(str.toLowerCase());
        break;
    case "6":
        alert(str.toUpperCase());
        break;
    case "7":
        let charToModify = prompt("Введите букву, которую нужно изменить");
        alert(str.replaceAll(charToModify, charToModify + "!!!"));
        break;
}