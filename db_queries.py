create_covid_data_table = """

CREATE TABLE IF NOT EXISTS ARC_insights_dp.covid_data (
	date date PRIMARY KEY,
	name varchar,
	code varchar,
	dailyCases float,
	cumulativeCases float,
	dailyDeaths float,
	cumulativeDeaths float,
	hospitalCases float,
	newReinfectionsBySpecimenDate float
);
"""
insert_covid_data_table = """INSERT INTO ARC_insights_dp.covid_data ('{}', '{}', '{}', '{}', {}, '{}', {}, {}, {})
                        ON CONFLICT (date)
                        DO UPDATE SET
                        date = EXCLUDED.date,
                        name = EXCLUDED.name,
                        code = EXCLUDED.code,
                        dailyCases = EXCLUDED.dailyCases,
                        cumulativeCases = EXCLUDED.cumulativeCases,
                        dailyDeaths = EXCLUDED.dailyDeaths,
                        cumulativeDeaths = EXCLUDED.cumulativeDeaths,
                        hospitalCases = EXCLUDED.hospitalCases,
                        newReinfectionsBySpecimenDate = EXCLUDED.newReinfectionsBySpecimenDate;
                        """