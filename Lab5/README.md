# Project Overview

**Goal**: The farm manager can see through all the operations in different fields.

**User**: manager at ACRE.
Can use this webpage to keep tracks of different details in the fields.

**Data Dictionary**
Variable | Scope | Description | Acceptable Values | Data Type
-----|-----|-----|-----|-----
field_num | Class | ACRE field ID Number | >0 | int
field_name | Field, Attribute | Name of the field | 50 characters | String
soil_type | Attribute | Soil type of the field | 50 characters | String
location | Attribute | location of the field | 50 characters | String
scientific_name | Class | scientific name of the crop | 50 characters | String
crop_name | Attribute | common name of the crop | 50 characters | String
life_form | Attribute | life form of the crop | 50 characters | String
chemical_type | Attribute | type of applied chemical | 50 characters | String
date_applied | Attribute | date and time of application | datetime | datetime
chemical_name | Class | name of the applied chemical | 50 characters | String
