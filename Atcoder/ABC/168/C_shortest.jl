a,b,h,m=parse.(Int64,split(readline()));print((a^2+b^2-2a*b*cos(11π*m/360-h*π/6))^.5)