#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import TemperatureConverter class in Jupyter
# Try importing from the notebook first, fallback to Python script if necessary

try:
    get_ipython().run_line_magic('run', 'temperature_converter.ipynb')
except:
    from temperature_converter import TemperatureConverter


def test_celsius_to_fahrenheit():
    converter = TemperatureConverter()
    assert converter.celsius_to_fahrenheit(0) == 32
    assert converter.celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius():
    converter = TemperatureConverter()
    assert converter.fahrenheit_to_celsius(32) == 0
    assert converter.fahrenheit_to_celsius(212) == 100

def test_celsius_to_kelvin():
    converter = TemperatureConverter()
    assert converter.celsius_to_kelvin(0) == 273.15
    assert converter.celsius_to_kelvin(100) == 373.15

def test_kelvin_to_celsius():
    converter = TemperatureConverter()
    assert converter.kelvin_to_celsius(273.15) == 0
    assert converter.kelvin_to_celsius(373.15) == 100

# Verify the import by creating an instance of TemperatureConverter
converter = TemperatureConverter()

# Test one function, for example:
print(converter.celsius_to_fahrenheit(0))


# In[ ]:




