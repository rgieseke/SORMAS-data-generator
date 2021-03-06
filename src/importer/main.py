import logging
import os
from datetime import date

import click

from universe.world import World

LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG').upper()

logging.basicConfig(
    level=LOGLEVEL,
    format='%(asctime)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s',
)


@click.command()
@click.option('--case-count', default=3, help='Number of cases you want to import.')
@click.option('--event-count', default=2, help='Number of events you want to import.')
def main(case_count, event_count):
    logging.info(f'Importing {case_count} cases')
    logging.info(f'Importing {event_count} events')
    # Set everything up
    # Create our world where we simulate a pandemic. This is our playground.
    # Set a beginning for our world

    world = World(date.fromisoformat('2020-02-01'))

    # Populate default entities in our world
    # Counties of interest
    lower_saxony = 'Niedersachsen'
    world.add_region(lower_saxony)
    world.add_district('Braunschweig', lower_saxony)
    world.add_district('Salzgitter', lower_saxony)
    world.add_district('Wolfsburg', lower_saxony)

    world.pre_populate_cases_and_contacts(n=case_count)

    # world.pre_populate_infection_chains() #todo
    #  ### Geolocations --- todo don't know yet
    world.pre_populate_events_and_participants(n=event_count)

    # Great, now store the world's case history in SORMAS/JSON/CSV etc
    world.export_sormas()
    # world.export_json()


if __name__ == '__main__':
    main()
