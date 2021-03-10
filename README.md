# Package-Delivery
The package delivery program was built as a project for my "Data Structures and Algorithms-2" computer science class. This project is a variant of the traveling salesperson problem set up as a package delivery company trying to optimize the mileage of it's deliveries. Using object-oriented design principles, I was required to build a program to model the delivery of the company's packages. I was given a .csv list of 40 packages and their distance data. These 40 packages would need to be delivered as optimally as possible by the end of the day. This task required the use of a self-adjusting heuristic algorithm, and a hashtable to keep the program scaleable and efficient. The following list outlines the delivery program's objectives and constraints.

1.   There are 3 delivery trucks and only 2 delivery drivers. Only 2 Trucks can deliver at a time.
2.   The truck's average speed is 18 MPH. Stop time(fueling and traffic) is calculated into the average speed.
3.  The delivery day starts no sooner than 8:00 am. The trucks cannot leave before this start time.
4.  Loading the truck's payload happens instantaneously. This is calculated into the average speed mentioned above.
5.  Each package delivery constraint must be followed according to the PackageData.csv file.
Example constraints are the following:(Must be delivered on specific truck, Cannot leave delivery hub until specified time, and Must be delivered with another package.)
6.  The distance data between addresses is provided in the PackageDistance.csv file.
7. The day ends when all of the packages have been delivered.