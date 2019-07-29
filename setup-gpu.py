from setuptools import setup, find_packages

setup(name='nomeroff-net',
      version='0.3.5',
      description='Automatic numberplate recognition system',
      long_description='Nomeroff Net is a opensource python license plate recognition framework based on the application of a convolutional neural network on the Mask_RCNN architecture, and cusomized OCR-module powered by GRU architecture. The project is now at the initial stage of development, write to us if you are interested in helping us in the formation of a dataset for your country.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: NU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
      keywords='Nomeroff Net ai  Mask_RCNN OCR GRU opensource license number plate recognition licenseplate numberplate license-plate number-plate ria-com RIA.com ria',
      url='https://github.com/ria-com/nomeroff-net',
      author='Dmytro Probachay, Oleg Cherniy',
      author_email='dimabendera@gmail.com, oleg.cherniy@ria.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'GitPython',
          'numpy',
          'matplotlib',
          'Keras',
          'Cython',
          'pycocotools',
          'matplotlib',
          'tensorflow-gpu',
          'opencv_python',
          'imutils',
          'scikit_image',
          'jupyter',
          'asyncio',
          'imgaug'
      ],
      include_package_data=True,
      zip_safe=False)