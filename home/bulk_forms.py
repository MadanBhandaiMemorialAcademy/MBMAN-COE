from django import forms

class BulkSemesterForm(forms.Form):
    number_of_semesters = forms.IntegerField(
        min_value=1, 
        max_value=12, 
        initial=8,
        label="Number of Semesters to Add",
        help_text="How many semesters do you want to create?"
    )
    start_from = forms.IntegerField(
        min_value=1,
        initial=1,
        label="Start from Semester Number",
        help_text="e.g. Start from 1 to create Semester 1, 2, 3..."
    )

class BulkCourseForm(forms.Form):
    course_data = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 10, 
            "class": "form-textarea w-full font-mono text-sm",
            "placeholder": "e.g.\nBIT101, Computer Fundamentals, 3\nBIT102, Digital Logic, 3"
        }),
        help_text="Enter each course on a new line in format: Code, Title, Credits",
        label="Course Data (CSV Format)"
    )

class BulkSemesterDeleteForm(forms.Form):
    semesters = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        label="Select Semesters to Delete",
        help_text="Warning: Deleting a semester will also delete all courses within it."
    )

    def __init__(self, *args, **kwargs):
        curriculum = kwargs.pop('curriculum', None)
        super().__init__(*args, **kwargs)
        if curriculum:
            self.fields['semesters'].queryset = curriculum.semesters.all().order_by('semester_number')

class BulkCourseDeleteForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        label="Select Courses to Delete"
    )

    def __init__(self, *args, **kwargs):
        semester = kwargs.pop('semester', None)
        super().__init__(*args, **kwargs)
        if semester:
            self.fields['courses'].queryset = semester.courses.all().order_by('display_order', 'code')
