height = 1.75;
weight = 8.05;

ming = int(weight/height);

if ming<=18.5:
	print('过轻')
elif 25>=ming and ming>=18.5:
	print('正常')
elif 28>=ming and ming>=25:
	print('过重')
elif 32>=ming and ming>=28:
	print('肥胖')
elif ming>=32:
	print('严重肥胖')

