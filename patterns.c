/*
Author: Sergiu Mosanu, 6/22/2023

input is 01010001110110111111000010110100

for clarity, I implemented 2 functions, one only finds one pattern, the second finds all patterns

pattern is "111"
patterns[] = {"111", "1101", "100001"};
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// function to initialize a string of length len to repeated value and ending with '\0'
void strinit(char* strtoinit, char value, int len){
    for(int j = 0; j < len; j++){
        strtoinit[j] = '0';
    }
    strtoinit[len] = '\0';
}

// function to update a string segment of length len, shift values to the left by 1, append a value
// example: '010'+1 becomes '101'
void updatestrsegment(char* strsegtoupdate, char value, int len){
    for(int j = 0; j < len-1; j++){
        strsegtoupdate[j] = strsegtoupdate[j+1];
    }
    strsegtoupdate[len-1] = value;
}

void onepatternmatch(char* inpstream, char* outstream, char* patterns[]){
    char* pattern = patterns[0]; // pick one of the patterns
    int pattern_len = strlen(pattern);

    // will store a segment of the input stream to compare with pattern
    char inpstream_segment[pattern_len]; // declare
    strinit(inpstream_segment, '0', pattern_len); // initialize to all '0's
    
    int i = 0;
    // while loop over input stream inpstream
    // at each new inpstream value:
    //     1) update inpstream_segment and 
    //     2) compare with pattern to determine outstream[i]
    while(inpstream[i] != '\0'){
        // update inpstream_segment
        updatestrsegment(inpstream_segment, inpstream[i], pattern_len);
        
        // determine outstream[i] by comparing inpstream_segment with pattern
        outstream[i] = (strcmp(inpstream_segment, pattern)==0) ? '1' : '0';

        i += 1;
    }
    outstream[i] = '\0'; // termination character
}

void allpatternsmatch(char* inpstream, char* outstream, char* patterns[], int patterns_count){
    int patterns_lenths[patterns_count];
    for(int j = 0; j < patterns_count; j++){
        patterns_lenths[j] = strlen(patterns[j]);
    }

    // will store segments of the input stream to compare with patterns
    char** inpstream_segments = malloc(patterns_count * sizeof(char*));
    for (int j = 0; j < patterns_count; j++) {
        // Allocate memory for the string
        inpstream_segments[j] = malloc((patterns_lenths[j] + 1) * sizeof(char));
        // Initialize the string to all '0's
        strinit(inpstream_segments[j], '0', patterns_lenths[j]);
    }

    
    int i = 0;
    // while loop over input stream inpstream
    // at each new inpstream value:
    //     1) update inpstream_segments and 
    //     2) compare with patterns to determine outstream[i]
    while(inpstream[i] != '\0'){
        // update inpstream_segments
        for (int j = 0; j < patterns_count; j++) {
            updatestrsegment(inpstream_segments[j], inpstream[i], patterns_lenths[j]);
        }
        // compare
        outstream[i] = '0'; // will do logic OR between each pattern compare
        for (int j = 0; j < patterns_count; j++) {
            outstream[i] = (outstream[i] == '1') || (strcmp(inpstream_segments[j], patterns[j])==0) ? '1' : '0';
        }

        i += 1;
    }
    outstream[i] = '\0'; // termination character
}

int main()
{
    // test input stream and output stream strings of any length
    char* inpstream = "01010001110110111111000010110100";
    printf("inpstream: %s\n", inpstream);
    char outstream_onepattern[strlen(inpstream)];
    char outstream_allpatterns[strlen(inpstream)];

    // pattern to be found as string of any length
    char* patterns[] = {"111", "1101", "100001"};
    int patterns_count = sizeof(patterns) / sizeof(char*);

    // compute outstreams by running the functions
    onepatternmatch(inpstream, outstream_onepattern, patterns);
    printf("out one p: %s\n", outstream_onepattern);
    allpatternsmatch(inpstream, outstream_allpatterns, patterns, patterns_count);
    printf("out all p: %s\n", outstream_allpatterns);

    return 0;
}
