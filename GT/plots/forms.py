from django import forms

class dfs_input_form(forms.Form):
    dropdown_choices = [
        ('mapusa', 'Mapusa'),
        ('panaji', 'Panaji'),
        ('margao', 'Margao'),
        ('ponda', 'Ponda'),
        ('vasco da gama', 'Vasco da Gama'),
        ('bicholim', 'Bicholim'),
        ('pernem', 'Pernem'),
        ('calangute', 'Calangute'),
        ('old goa', 'Old Goa'),
        ('valpoi', 'Valpoi'),
    ]
    
    Start = forms.ChoiceField(
        choices=dropdown_choices,
        widget=forms.Select(attrs={'class': ' block w-full h-20 rounded-2xl shadow-2xl border-2 appearance-none text-gray-950 pl-6'}),
    )

class a_star_form(forms.Form):
    dropdown_choices_start = [
        ('mapusa', 'Mapusa'),
        ('panaji', 'Panaji'),
        ('margao', 'Margao'),
        ('ponda', 'Ponda'),
        ('vasco da gama', 'Vasco da Gama'),
        ('bicholim', 'Bicholim'),
        ('pernem', 'Pernem'),
        ('calangute', 'Calangute'),
        ('old goa', 'Old Goa'),
        ('valpoi', 'Valpoi'),
    ]
    
    Start = forms.ChoiceField(
        choices=dropdown_choices_start,
        widget=forms.Select(attrs={'class': ' block w-full h-20 rounded-2xl shadow-2xl border-2 appearance-none text-gray-950 pl-6 mb-4'}),
    )

    dropdown_choices_end = [
        ('mapusa', 'Mapusa'),
        ('panaji', 'Panaji'),
        ('margao', 'Margao'),
        ('ponda', 'Ponda'),
        ('vasco da gama', 'Vasco da Gama'),
        ('bicholim', 'Bicholim'),
        ('pernem', 'Pernem'),
        ('calangute', 'Calangute'),
        ('old goa', 'Old Goa'),
        ('valpoi', 'Valpoi'),
    ]
    
    End = forms.ChoiceField(
        choices=dropdown_choices_end,
        widget=forms.Select(attrs={'class': ' block w-full h-20 rounded-2xl shadow-2xl border-2 appearance-none text-gray-950 pl-6'}),
    )

class deg_centrality_form(forms.Form):
    dropdown_choices = [
        ('mapusa', 'Mapusa'),
        ('panaji', 'Panaji'),
        ('margao', 'Margao'),
        ('ponda', 'Ponda'),
        ('vasco da gama', 'Vasco da Gama'),
        ('bicholim', 'Bicholim'),
        ('pernem', 'Pernem'),
        ('calangute', 'Calangute'),
        ('old goa', 'Old Goa'),
        ('valpoi', 'Valpoi'),
    ]
    
    Node = forms.ChoiceField(
        choices=dropdown_choices,
        widget=forms.Select(attrs={'class': ' block w-full h-20 rounded-2xl shadow-2xl border-2 appearance-none text-gray-950 pl-6'}),
    )

class radial_form(forms.Form):
    dropdown_choices = [
        ('mapusa', 'Mapusa'),
        ('panaji', 'Panaji'),
        ('margao', 'Margao'),
        ('ponda', 'Ponda'),
        ('vasco da gama', 'Vasco da Gama'),
        ('bicholim', 'Bicholim'),
        ('pernem', 'Pernem'),
        ('calangute', 'Calangute'),
        ('old goa', 'Old Goa'),
        ('valpoi', 'Valpoi'),
    ]

    
    Start = forms.ChoiceField(
        choices=dropdown_choices,
        widget=forms.Select(attrs={'class': ' block w-full h-20 rounded-2xl shadow-2xl border-2 appearance-none text-gray-950 pl-6'}),
    
    )

    radius_in_km = forms.DecimalField(
        label="Radius (in kilometers)",
        min_value=0.1, 
        widget=forms.NumberInput(attrs={'type': 'number', 'step': '0.01', 'class': ' block w-full h-20 rounded-2xl shadow-2xl border-2 appearance-none text-gray-950 pl-6'}),
    )