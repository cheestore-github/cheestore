from django.core.validators import RegexValidator



telephone_regex = RegexValidator(  
                                    regex=r'^([0-9]{3})?[0-9]{8}$', 
                                    message="telephone number must be either 8 or 11 digits."
                                )


zip_code_regex = RegexValidator(  
                                    regex=r'^\d{10}$', 
                                    message="zip code must be 10 digits exactly."
                                )