import random
from random import choice

from sormas import PersonReferenceDto, Sex, PresentCondition

from generator.utils import duuid
from universe.person import Person

random.seed(2)

# Maximum age that can be generated
max_age = 95

# todo BEGIN only german names for now b/c residence abroad cannot be displayed
male_first_names = [
    'Peter', 'Wolfgang', 'Michael', 'Werner', 'Klaus', 'Thomas',
    'Manfred', 'Helmut', 'Jürgen', 'Heinz', 'Gerhard', 'Andreas', 'Hans',
    'Josef', 'Günter', 'Dieter', 'Horst', 'Walter', 'Frank', 'Bernd', 'Karl',
    'Herbert', 'Franz ', 'Mehmet', 'Mustafa', 'Piotr', 'Krzysztof'
]
female_first_names = [
    'Maria', 'Ursula', 'Monika', 'Petra', 'Elisabeth', 'Sabine', 'Renate',
    'Helga', 'Karin', 'Brigitte', 'Ingrid', 'Erika', 'Andrea', 'Gisela',
    'Claudia', 'Susanne', 'Gabriele', 'Christa', 'Christine', 'Hildegard',
    'Anna', 'Birgit', 'Fatma', 'Ayşe '
]
last_names = [
    'Müller', 'Schmidt', 'Schneider', 'Fischer', 'Weber', 'Meyer',
    'Wagner', 'Becker', 'Schulz', 'Hoffmann', 'Schäfer', 'Koch', 'Bauer',
    'Richter', 'Klein', 'Wolf', 'Schröder', 'Neumann', 'Schwarz', 'Zimmermann',
    'Braun', 'Krüger', 'Hofmann', 'Yilmaz', 'Kaya', 'Nowak', 'Kowalski'
]
# todo END

# todo I don't now how state that a person does not live inside the jurisdiction/country of SORMAS
# todo I don't if this is even possible
# Default country of residence
default_country = 'Deutschland'
# Foreign country of residence taken as example
foreign_country = 'Frankreich'
# Probability that a case has residence abroad
p_foreign_country = 0.05


def country_of_residence():
    # todo
    pass


# todo END

# todo
# For cases, if they live in the default country, the address is the reporting
# local health authority with probability `p_lha_address` and any other county
# with uniform probability. If the reside abroad it is "abroad".
# todo END


def assign_age_from_rki_age_group(ag_vec, m_a):
    # Draws a random age in each age group of the vector `ag_vec` uniformly at
    # random. For the last age group "A80+", a maximum age of `m_a` is taken.
    # Specific to the way age groups are coded in RKI's corona dashboard
    # todo do this statically without the need of parsing a file each and every time we run the script
    pass


def assign_address():
    # todo
    pass


def gen_person_dto(first_name=None, last_name=None, sex=None, birthdate_yyyy=None, address=None, present_condition=None):
    if first_name is None:
        first_name = choice(male_first_names) if sex is Sex.MALE else choice(female_first_names)
    if last_name is None:
        last_name = choice(last_names)
    if sex is None:
        sex = choice([Sex.MALE, Sex.FEMALE])
    if birthdate_yyyy is None:
        birthdate_yyyy = random.randrange(10, 90)  # FIXME

    #fixme address can be none

    # Person extends PersonDto, but Person overwrites __str__ for better debugging
    person_dto = Person(
        uuid=duuid(),
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        birthdate_yyyy=birthdate_yyyy,
        address=address,
        present_condition=present_condition
    )
    return person_dto


def person_ref(person_uuid):
    person_ref_dto = PersonReferenceDto(uuid=person_uuid)
    return person_ref_dto
