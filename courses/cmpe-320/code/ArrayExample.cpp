
#include <iostream>
using namespace std;

void passArray1(int param[]) {
	cout << "Array size when passing int[]: " << sizeof(param) << endl;
	// So, how do we get the size of param inside this function?
}

void passArray2(int* param) {
	cout << "Array size when passing int*: " << sizeof(param) << endl;
	// Same problem here!
}

int main() {

	int i;
	int anArray[5];

	// What is in an uninitialized array?
	cout << "Uninitialized:\n";
	for(i = 0; i < 5; i++)
		cout << anArray[i] << endl;

	cout << "\nInitialized:\n";
	for(i = 0; i < 5; i++)
		anArray[i] = 100 * i;
	for(i = 0; i < 5; i++)
		cout << anArray[i] << endl;
	cout << "Size of anArray: " << sizeof(anArray) << endl;
	cout << "Number of elements in anArray: " << sizeof(anArray) / sizeof(int) << endl;
	// Use a vector instead!!!  Much easier to get the size.

	// What do I get when I try to print the entire array?
	cout << "Printing the array name: " << anArray << endl;

	// The array as a pointer:
	cout << "The address of the array: " << &anArray << endl;
	cout << "The address of the first element: " << &anArray[0] << endl;

	// Pointer arithmetic!
	cout << "\nDisplaying the array contents, as well as one position before and";
	cout << "\none position after using pointer arithmetic:\n";
	for(i = -1; i <= 5; i++)
		cout << *(anArray + i) << endl;
	cout << endl << *(anArray + 10) << endl;	// How far can I go?

	// Passing an array into a function.
	// How to get the size of the array in the function?
	passArray1(anArray);
	passArray2(anArray);

	cout << "\nMessing with array dimensions:" << endl;
	int bArray[] = {1, 2};
	bArray[0] = 100;
	bArray[1] = 200;
	bArray[2] = 300;
	for (i = 0; i < 3; i++)
		cout << bArray[i] << endl;
	cout << sizeof(bArray) << endl;

	// C Strings
	cout << "\nC Strings, Yuk:" << endl;
	char aString[] = "Hello";
	cout << aString << endl;
	aString[4] = 'p';
	cout << aString << endl;
	cout << sizeof(aString) << endl;

	char* bString = "Goodbye";	// Depreciated - don't do this anymore!
	//bString[4] = 'H';			// And really don't do this!

	const char* cString = "Hello Goodbye";	// This is fine.
	cout << cString << endl;
	cout << cString[6] << endl;
	//cString[6] = 'H';			// Not permitted because cString is const

	// Better to use the string class instead of C-strings...
	// Better to use vectors instead of arrays!

	return 0;
}
