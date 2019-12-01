def euclid_gcd(big,small):
	mod = big % small
	if mod == 0:
		return small
	else:
		return euclid_gcd(small,mod)


if __name__ == '__main__':
     print("1112 695 GCD is " + str(euclid_gcd(1112,695)))

     
     
