/*
 * This program declares examples of atomic types and determines their memory usage.
 * Also, the behaviour of integers is explored to see if they wrap around as in Java.
 *
 * Compile this program to the C++14 or C++17 standard.
 */
#include <iostream>
using namespace std;

enum MonthLengths {
	JAN = 31, FEB = 28, MAR = 31,
	APR = 30, MAY = 31, JUN = 30,
	JUL = 31, AUG = 31, SEP = 30,
	OCT = 31, NOV = 30, DEC = 31
};

int main() {

	// The C++14 standard allows for binary literals and grouping digits:
	int aVal(0b1100'0010'0001'1111);
	cout << "Binary number in base 10: " << aVal << endl << endl;

	bool b1(false);
	char c1('H');
	wchar_t c2(0x03b8);
	char16_t c3(0x03b8);		// C++11
	char32_t c4(0x000003b8);	// C++11

	// Integer types
	short s1(0);
	int iprod(1);
	long lprod(1L);
	long long llprod(1L);
	long long int lliprod(1L);	// C++11
	// Note that short can also be declared as "short int"
	// and long can be declared as "long int".

	// Floating point types
	float f1(2.5F);
	double d1(2.0);
	long double ld(2.0);

	// Get memory consumption
	cout << "bool: " << "\t\t" << sizeof(b1) << " byte\n";
	cout << "char: " << "\t\t" << sizeof(c1) << " byte\n";
	cout << "Wide char: " << "\t" << sizeof(c2) << " bytes\n";
	cout << "UTF-16 char: " << "\t" << sizeof(c3) << " bytes\n";
	cout << "UTF-32 char: " << "\t" << sizeof(c4) << " bytes\n";
	cout << "short: " << "\t\t" << sizeof(s1) << " bytes\n";
	cout << "int: " << "\t\t" << sizeof(iprod) << " bytes\n";
	cout << "long: " << "\t\t" << sizeof(lprod) << " bytes\n";
	cout << "long long: " << "\t" << sizeof(llprod) << " bytes\n";
	cout << "long long int: " << "\t" << sizeof(lliprod) << " bytes\n";
	cout << "float: " << "\t\t" << sizeof(f1) << " bytes\n";
	cout << "double: " << "\t" << sizeof(d1) << " bytes\n";
	cout << "long double: " << "\t" << sizeof(ld) << " bytes\n";

	// This also works:
	cout << "int again: " << "\t" << sizeof(int) << " bytes\n";

	// What happens if you don't initialize a variable (see Exercise 1)?
	double test;
	cout << "\nNot initialized: " << test << endl;

	const double ACONST(4.2e1);
	cout << "\nTesting a constant:" << endl;
	cout << ACONST << endl;
	// Try changing the constant
	//ACONST = 10e3;

	// Testing enum
	// Better to use enums with conditionals...
	cout << "\nTesting enum:" << endl;
	cout << FEB << endl;
	MonthLengths aMonth = MAR;
	cout << aMonth << endl;
	cout << (aMonth == MAR) << endl;

	// Booleans:
	cout << "\nWhat is true or false?:" << endl;
	cout << "true is: " << true << endl;
	cout << "false is: " << false << endl;
	cout << "true takes " << sizeof(true) << " byte." << endl;

	cout << "\nTesting wrapping of integers:\n";
	cout << "For the int type:" << endl;
	for (int mult = 2; mult <= 25; mult++) {
		iprod *= mult;
		cout << mult << "! is " << iprod << endl;
	}

	cout << "\nFor the long long type:" << endl;
	for (int mult = 2; mult <= 25; mult++) {
		llprod *= mult;
		cout << mult << "! is " << llprod << endl;
	}

	return 0;
}
