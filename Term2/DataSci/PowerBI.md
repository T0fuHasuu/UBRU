# **Power BI**

1. **What is Power BI?**  
   **Answer:** Power BI is a business intelligence (BI) tool by Microsoft that provides interactive data visualization, analytics, and reporting capabilities.

2. **What are the key components of Power BI?**  
   **Answer:**  
   - **Power BI Desktop** – Used for report creation  
   - **Power BI Service (Cloud)** – Used for sharing and collaboration  
   - **Power BI Mobile** – Used for viewing reports on mobile devices  
   - **Power BI Gateway** – Connects cloud reports to on-premise data  

3. **What data sources can Power BI connect to?**  
   **Answer:** Power BI supports **SQL Server, Excel, Azure, SharePoint, Google Analytics, JSON, CSV, APIs**, and more.

4. **What is Power Query?**  
   **Answer:** Power Query is a data transformation and ETL (Extract, Transform, Load) tool in Power BI used for **cleaning, transforming, and preparing data**.

5. **What is Power Pivot?**  
   **Answer:** Power Pivot is a **data modeling tool** in Power BI that helps in **creating relationships between tables and performing calculations** using **DAX (Data Analysis Expressions)**.

---

## **Intermediate Power BI Questions**

6. **What is DAX in Power BI?**  
   **Answer:** DAX (Data Analysis Expressions) is a formula language in Power BI used for **calculating measures, aggregations, and computed columns**.

7. **What are the types of filters in Power BI?**  
   **Answer:**  
   - **Visual-level filter** – Filters a single visualization  
   - **Page-level filter** – Filters all visuals on a single page  
   - **Report-level filter** – Filters all visuals across pages  
   - **Drill-through filter** – Allows detailed analysis of specific data points  

8. **What are calculated columns in Power BI?**  
   **Answer:** Calculated columns are new columns created in a table using **DAX expressions** that are computed **row by row**.

9. **What is a measure in Power BI?**  
   **Answer:** A measure is a **calculated field** used for aggregations like SUM, AVG, COUNT, and is evaluated dynamically based on filters.

10. **What is the difference between a calculated column and a measure?**  
   **Answer:**  
   - **Calculated Column** – Computed at the row level, stored in the table  
   - **Measure** – Computed dynamically, does not store data  

11. **What is a relationship in Power BI?**  
   **Answer:** A relationship connects two tables using **primary and foreign keys**, allowing Power BI to **combine data from different tables**.

12. **What are the different types of relationships in Power BI?**  
   **Answer:**  
   - **One-to-One (1:1)**  
   - **One-to-Many (1:M)**  
   - **Many-to-Many (M:M)**  

13. **What is a KPI in Power BI?**  
   **Answer:** A KPI (Key Performance Indicator) is a **visualization that tracks key business metrics** using a base value, target value, and status.

14. **How can you refresh data in Power BI?**  
   **Answer:**  
   - **Manual refresh** – Click "Refresh" in Power BI Desktop  
   - **Scheduled refresh** – Set automatic updates in Power BI Service  
   - **Live connection** – Direct connection updates automatically  

15. **What is the difference between DirectQuery and Import Mode in Power BI?**  
   **Answer:**  
   - **Import Mode** – Loads data into Power BI, offers fast performance  
   - **DirectQuery Mode** – Queries data **directly from the source**, useful for real-time analysis  

---

## **Advanced Power BI Questions**

16. **What is Row-Level Security (RLS) in Power BI?**  
   **Answer:** RLS restricts **user access to specific data rows** based on their roles, implemented using **DAX expressions**.

17. **What is a Power BI dashboard?**  
   **Answer:** A dashboard is a **single-page, interactive report** containing multiple visuals from different datasets.

18. **How can you share reports in Power BI?**  
   **Answer:**  
   - **Power BI Service** (via workspace)  
   - **Publish to web** (for public sharing)  
   - **Export to PDF/PPT**  
   - **Power BI Embedded** (embed in applications)  

19. **What are bookmarks in Power BI?**  
   **Answer:** Bookmarks **save the current state of a report**, including filters, slicers, and selections for quick navigation.

20. **What is Drill-through in Power BI?**  
   **Answer:** Drill-through allows users to **click on a visual** and navigate to a detailed report focusing on that specific data.

21. **What is a tooltip in Power BI?**  
   **Answer:** A tooltip is a **hover-over popup** that displays additional information about a visual element.

22. **How can you optimize Power BI performance?**  
   **Answer:**  
   - Use **aggregations** instead of raw data  
   - Reduce **cardinality** of columns  
   - Use **DirectQuery for large datasets**  
   - Optimize **DAX calculations**  

23. **What is the difference between SUM() and SUMX() in Power BI?**  
   **Answer:**  
   - **SUM()** – Aggregates a column  
   - **SUMX()** – Iterates through each row, evaluates an expression, then sums  

24. **What is Power BI Gateway?**  
   **Answer:** Power BI Gateway is a **bridge that connects on-premise data sources** to the Power BI cloud.

25. **What are Hierarchies in Power BI?**  
   **Answer:** Hierarchies define **multi-level drill-down structures** (e.g., Year → Quarter → Month → Day).

---

## **Scenario-Based Power BI Questions**

26. **How do you handle missing data in Power BI?**  
   **Answer:**  
   - Use **Power Query** to replace nulls with a default value  
   - Use **DAX functions** like `IF(ISBLANK())`  

27. **How would you create a Year-to-Date (YTD) measure in Power BI?**  
   **Answer:**  
   ```DAX
   YTD_Sales = TOTALYTD(SUM(Sales[Amount]), Dates[Date])
   ```
   This calculates cumulative sales from the start of the year to the current date.

28. **How do you remove duplicate values in Power BI?**  
   **Answer:**  
   - Use **Remove Duplicates** in Power Query  
   - Use `DISTINCT()` function in DAX  

29. **If your Power BI report is slow, how would you troubleshoot?**  
   **Answer:**  
   - **Reduce data size** by filtering  
   - **Optimize DAX queries**  
   - **Use Import Mode instead of DirectQuery**  

30. **How do you create a dynamic slicer in Power BI?**  
   **Answer:**  
   - Create a **calculated table** using `VALUES()`  
   - Use `SELECTEDVALUE()` to capture slicer selection  

