""" Printing the names of city and country"""
def city_country_name(city, country,population=''):
	if population:
		full_name = f"{city},{country} {population}"
	else:
			full_name = f"{city},{country}"

	return full_name.title()