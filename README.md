This is a DBMS project based on an AI generated dataset, which practiced from building the ERD to establishing the full-stack web API.
Project detail can be examined in [pptx](https://github.com/zcry332/DBMS/raw/refs/heads/main/ZhenjunHuang&XinHuang-DBTermProject/DB-Project-WriteUp.docx).

# Project Overview
*Our project is to create a travel agency booking database that facilitates and manages booking flights and hotels for customers. This system will allow travel agencies to efficiently track customer preferences, predict travel costs, and optimize travel options based on budget constraints.
The team members of this project are Zhenjun Huang and Xin Huang*
# Problem to Solve
_This database helps select travel plans based on trip duration, suggests affordable accommodations, and promotes the most suitable plan for customers_

## Primary Entities
### Customer:
- Customer ID (PK)
- First name
- Middle name
- Last name
- Email
### Orders
- Order ID (PK)
- Customer ID (FK referencing Customer)
- Trip ID (FK referencing Trip)
- Start date
- finish date
- Booking status
- Total price
### Ratings
- Rating ID (PK)
- Customer ID (FK referencing Customer)
- Order ID (FK referencing Orders)
- Rating score (1~5)
- Feedback/comment
- Rating date
### Trip
- Trip ID (PK)
- Trip name
- Description
- Duration (days)
- Trip type (e.g., adventure, relaxation, cultural)
- Base price
### Flight
- Flight ID (PK)
- Trip ID (FK referencing Trip) - if the flight is part of a package
- Airline name
- Flight number
- Departure airport
- Arrival airport
- Departure date/time
- Arrival date/time
- Price
- Class (economy, business, first)
### Hotel
- Hotel ID (PK)
- Name
- Address
- City
- Country
- Star rating
- Amenities
- Contact information
### Hotel_Trip (Junction table for many-to-many relationship)
- Hotel_Trip ID (PK)
- Hotel ID (FK referencing Hotel)
- Trip ID (FK referencing Trip)
- Room type
- Price per night

## Data Sources
The data for this project will be using AI-generated datasets to simulate realistic booking scenarios.
 
## Business Rules
- Each customer must have a unique email.
- Customers cannot book the same hotel twice.
- Customers must depart from the same city as they arrived in.
- A booking must be linked to an existing trip.
- Ratings can only be submitted after a completed trip.
- Ratings below three stars are flagged as complaints.
 
## Views
1. Booking Overview: Displays combined hotel and flight bookings with date to track and manage reservations.
2. Customer Satisfaction Summary: Shows other customer ratings and complaints to monitor service quality and identify issues.
 
## Queries (as Stored Procedures)
1. Identifies high-demand destinations(top 5/10) based on booking trends.
2. Predict affordable accommodations based on a given budget range.
3. Predict optimal travel days(cheapest).
4. Hide low rating options for customers to select.
## Triggers
1. Auto-flag low ratings: if a rating is below 3, it is marked as low priority.
2. Ensures duration is positive and within reasonable limits
3. When an order is canceled, update inventory availability
4. After a new rating is added, recalculate and update the average rating for the trip
5. Ensure proper cascading of updates/deletes across related tables
## User Interfaces
- Create, modify, and cancel reservations.
- Add, update, and remove travel options.
- Trip search and filtering (by duration, price, etc.)
- Booking workflow with date selection
- Trip details view
- Rating and feedback submission form
- Booking history and status tracking
