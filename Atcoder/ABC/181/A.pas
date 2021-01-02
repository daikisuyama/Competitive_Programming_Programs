var
    n:Smallint;
begin
	read(n);
    if (n mod 2)=1 then
        writeln('Black')
    else
        writeln('White');
end.