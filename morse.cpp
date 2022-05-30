#pragma once

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <utility>

// define map<string, string>

std::string s_pattern[26] = { ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.." };
std::string l_pattern[26] = { "A","B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };

struct MorseNode {
    std::string letter;
    std::string simbol;
    MorseNode* dot;
    MorseNode* dash;

    MorseNode(std::string letter, std::string simbol) : letter(letter), simbol(simbol), dot(nullptr), dash(nullptr) {}

};

MorseNode root = MorseNode("", "");


std::vector<std::string > possibilities(const std::string& word) {
    
   
    std::cout << "possibilities for ---" << word << std::endl;
    for (int i = 0; i < 26; i++) {
        std::string morseSimbol = s_pattern[i];
        //build trie data structure
        MorseNode* node = &root;
        while (morseSimbol.length() > 0) {
            if (morseSimbol[0] == '.') {
                if (node->dot == nullptr) {
                    node->dot = new MorseNode("", "");
                }
                node = node->dot;
            }
            else {
                if (node->dash == nullptr) {
                    node->dash = new MorseNode("", "");
                }
                node = node->dash;
            }
            morseSimbol = morseSimbol.substr(1);

        }
        node->letter = l_pattern[i];
    }

    // word is a morse code with ., - and ?
    // when we find a ? the simbol could be either a dot or a dash
    // return all possible words generated from the morse code
    std::vector<std::string> result;
    MorseNode* node = &root;
    void findPossibilities(MorseNode* root, std::string code, std::vector<std::string> result){
        if (code.length() == 0) {
            result.push_back(root->letter);
            return;
        }
        if (code[0] == '.') {
            findPossibilities(root->dot, code.substr(1), result);
        }
        else if (word[0] == '-') {
            findPossibilities(root->dash, code.substr(1), result);
        }
        else {
            findPossibilities(root->dot, code.substr(1), result);
            findPossibilities(root->dash, code.substr(1), result);
        }

    }
    findPossibilities(node, word, result);
    return result;
}