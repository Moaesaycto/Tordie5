from setuptools import setup, find_packages

setup(
    name='tordie',
    version='0.1.0',
    author='Moaesaycto',
    author_email='your.email@example.com',
    description='A library for creating and manipulating SVG graphics',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_svg_lib',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
        # Example: 'numpy>=1.18.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12.4',
)
