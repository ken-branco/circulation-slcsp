from collections import OrderedDict, defaultdict


zip_rate = OrderedDict()
state_area_rate = defaultdict(list)
zip_state_area = OrderedDict()


def load_file_data():
    with open('files/slcsp.csv', 'r') as zc:
        for line in zc.readlines()[1:]:
            (zip_code, _) = line.strip().split(',')
            zip_rate.update({zip_code: None})

    with open('files/zips.csv', 'r') as zs:
        for line in zs.readlines()[1:]:
            # no use for county and name
            (zip_code, state, _, _, rate_area ) = line.strip().split(',')
            if zip_code not in zip_state_area.keys():
                zip_state_area.update({zip_code: set()})
            else:
                zip_state_area[zip_code].add(f"{state}-{rate_area}")

    with open('files/plans.csv', 'r') as zp:
        for line in zp.readlines()[1:]:
            # no use for county and name
            (_, state, metal_level, rate, rate_area ) = line.strip().split(',')
            if metal_level != "Silver":
                continue
            state_area = f"{state}-{rate_area}"
            if state_area not in state_area_rate.keys():
                state_area_rate.update({state_area: [rate]})
            else:
                state_area_rate[state_area].append(rate)


def fill_zip_rates():
    for zip_code, rate in zip_rate.items():
        silver_plan_rates = []
        zip_state_areas = zip_state_area[zip_code]

        if not zip_state_areas or len(zip_state_areas) > 1:
            zip_rate[zip_code] = ''
            continue
        for area in zip_state_areas: # should always be 1, but extract for key use below
            silver_plan_rates.extend(state_area_rate[area])

        if silver_plan_rates:
            zip_rate[zip_code] = sorted(silver_plan_rates)[1]

        pass


# if __name__ == "main":
load_file_data()
fill_zip_rates()

for zip, rate in zip_rate.items():
    print(f"{zip},{rate}")


pass