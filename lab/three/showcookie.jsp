<html>
<body>
<h3>Reading the cookies</h3>
<%
Cookie[] array= request.getCookies();
for(int i=0; i<array.length; i++)
{
if(array[i].getName().equals("username"))
{
out.println("<br/>");
out.println("Name of the cookie : " + array[i].getName() + "<br/>");
out.println("Value in cookie : " + array[i].getValue());
}
}
%>
</body>
</html>
