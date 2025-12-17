---
id: 1657
title: 'Example Programs'
date: '2012-06-21T12:27:00-07:00'
author: wandell
layout: page
guid: 'http://www.stanford.edu/group/vista/cgi-bin/FOV/?page_id=1657'
---

The links on this page explain specific computations from the book. At present, these computations include image formation, cone absorption characteristics, and color matching and discrimination. Other topics will be added over time.

The computations are written in Matlab and rely on a set of integrated tools for modeling visual encoding and early visual system processing ([ISETBIO](https://github.com/isetbio/isetbio)) The code is freely available on [gitub](https://github.com/isetbio/isetbio).

There is a brief description of each computation on this page. The code and comments on the linked pages are much more extensive.

Note: For this page, clicking on a link generally opens the link in a new TAB or WINDOW.

## ISETBIO Programming

The links below use the ISETBIO programming tools and explain the philosophy of the software organization. If you plan to use ISETBIO, these links should be useful to you. You should know that (a) ISETBIO is derived from a more general tool built by Imageval Consulting, LLC, called the [Image Systems Engineering Toolbox (ISET)](http://imageval.com/), and (b) ISET does more, is appropriate for industry use, and costs money. ISETBIO is a subset of ISET that is appropriate for modeling the front-end of the human visual system and is free. Some of the links below refer to ISET and some to ISETBIO because, well, I haven’t developed a great plan for separating the two in the documentation.

[ISETBIO Scene object](http://white.stanford.edu/~brian/FOV/tutorials/t_IntroductionScene.html)

ISETBIO input is a spectral radiance description of the scene. Various types of scenes can be constructed automatically, hyper spectral images can be read in and turned into scenes, and RGB scenes can be read in and converted to scenes based on a display model calibration.

[ISETBIO Optical Image object](http://white.stanford.edu/~brian/FOV/tutorials/t_IntroductionOI.html)

The transformation of a scene spectral radiance image to a spectral irradiance image at the sensor (or retinal) surface depends on the properties of the optics. The ISETBIO object representing the spectral irradiance image is called the optical image (OI). The OI structure includes a definition of the optics, which can be based either on diffraction limited optics, shift-invariant optics, or a shift-variant ray tracing model.

## Optics

[Human optics: Part I](http://white.stanford.edu/~brian/FOV/tutorials/s_HumanOptics.html)

The line spread function is a simple measure of the quality of the optics. This script illustrates the ISET routines that implement Marimont and Wandell’s model of the human optics.

[Human optics: Part II ](http://white.stanford.edu/~brian/FOV/tutorials/s_HumanLSF.html)

This tutorial shows images of the line spread that quantify the wavelength dependence of the line spread. It also includes point spreads, optical transfer functions (OTF), and two standard polychromatic line spread functions.

[Human optics: adaptive optics](http://white.stanford.edu/~brian/FOV/tutorials/s_wvfThibosModel.html)

Adaptive optics has produced many measurements of human wavefront aberrations. A standard model of the average subject is evolving. The code in this script, being developed in collaboration with Heidi Hofer and David Brainard, implements a standard observer proposed by Larry Thibos.

## Cone absorptions

[Photon absorptions in the cone mosaic](http://white.stanford.edu/~brian/FOV/tutorials/s_HumanSensor.html)

The rate or number of photon absorptions in each type of cone is a fundamental physical factor that limits our ability to detect light, discriminate colors, and estimate form. The calculations in this script illustrate how to compute the photon absorption rates.

[Spatial pattern of cone absorptions](http://white.stanford.edu/~brian/FOV/tutorials/s_HumanSceneStatistics.html)

A white noise scene (Gaussian independent at each point, D65 spectral power distribution) is transformed by passing through the human optics. This script shows how the spatial frequency of the white noise distribution becomes a ‘blue noise’ distribution at the cone mosaic.

## Color

[Color matching: metamerism](http://white.stanford.edu/~brian/FOV/tutorials/t_ColorMetamerism.html)

Two stimuli with different spectral power distributions may still have the same effect on the three types of cones. A pair of physically different stimuli that have the same effect on the cone absorptions are called metamers. This script constructs a pair of metamers and follows them through the optics into the cone absorptions.

[Wavelength discrimination and mean illumination](http://white.stanford.edu/~brian/FOV/tutorials/s_HumanWavelengthDiscrimination.html "Wavelength Discrimination")

The ability to discriminate two different wavelengths depends on the mean level of illumination. At low levels the photon noise is a significant factor. This script calculates the discriminability of a pair of wavelengths as a function of the mean illumination level.

## Online lectures and tutorials

Click on the [Talks and Tutorials Tab](http://www.stanford.edu/group/vista/cgi-bin/wandell/talks-and-tutorials/) of [Wandell’s home page ](http://www.stanford.edu/group/vista/cgi-bin/wandell/)for a more complete list.

[Lectures from Winter 2012 (videos from talks.stanford.edu).](https://talks.stanford.edu/applied-vision-and-image-systems-psych-221/)

- [Spectral Radiance Units](http://white.stanford.edu/~brian/Videos/Psych221/Spectral%20Radiance%20Units/Spectral%20Radiance%20Units.html)
- [Measuring Radiance](http://white.stanford.edu/~brian/Videos/Psych221/Measuring%20Radiance/Measuring%20Radiance.html)
- [Spectral irradiance](http://white.stanford.edu/~brian/Videos/Psych221/Spectral%20Irradiance/Spectral%20Irradiance.html)
- [Linear Models](http://white.stanford.edu/~brian/Videos/Psych221/Linear%20Models/Linear%20Models.html)