<html>
<head>
    <title>Java Bean Demo</title>
</head>
<body>
    <jsp:useBean id="employee" class="college.Employee" />

    <h2>Employee details</h2>
    Name: <jsp:getProperty name="employee" property="name" /><br/>
    Department: <jsp:getProperty name="employee" property="department" /><br/>

    <jsp:setProperty name="employee" property="name" value="Durga" />
    <jsp:setProperty name="employee" property="department" value="CSE" />

    <h2>New Employee details</h2>
    Name: <jsp:getProperty name="employee" property="name" /><br/>
    Department: <jsp:getProperty name="employee" property="department" /><br/>
</body>
</html>
