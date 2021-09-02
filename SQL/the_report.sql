/*
Enter your query here.
*/
with grade_info as (
    select
        Grade
        , floor(Min_Mark/10) as grade_mark
    from
        Grades
), students_info as (
    select
        id
        , name
        , marks
        , if(marks=100, 9, floor(marks/10)) as grade_mark
    from
        students
), students_grade_info as (
    select
        t1.id
        ,t1.name
        , t1.marks
        , t2.grade
    from
        students_info t1
    left join
        grade_info t2
    on
        t1.grade_mark=t2.grade_mark
)
select
    if(grade<8, Null, name) as name
    , grade
    , marks
from
    students_grade_info
order by
    grade desc, name, marks asc