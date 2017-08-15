# Paywalls Suck

Web app written in Flask/Flask-restful to generate a screengrab from a given URL.

## Whats here?

Web app and a simple API

## Disclaimer

* YMMV, this is a personal project. Whilst it is working for me, due to the OS specific nature of PhantomJS, something might break for you. 

* Not all pages may render the way you will see in a Chhrom(ium)e, Firefox, Etc, this can be due to setTimeout or a plethora of other JS libs running on the site that renders the site in a time specific manner.

## Background

I was stuck without internet for a day, I wanted to make something using whatever leftover existing libraries I had contained within some other projects. I also wanted to create a RESTful API for the purpose of grabbing screengrabs of sites that have some form of paywall.

### Requirements

See requirements.txt or simply


```
pip install -r requirements.txt
```

## API Usage

<table class="table table-bordered">
	<tbody>
		<tr>
			<th>End Point</th><td>/api/grab</td>
		</tr>
		<tr>
			<th>Keys</th><td>url (required), width (optional), height (optional)</td>
		</tr>
		<tr>
			<th>Headers</th><td>api_key  (required)</td>
		</tr>
		<tr>
			<th>Return Value</th><td>{'url':'filename.png'}</td>
		</tr>
	</tbody>
</table>

### Libraries used

* [Flask](https://flask.pocoo.org)
* [Flask Restful](https://flask-restful.readthedocs.io)
* [PhantomJS](https://phantomjs.org)
* [Selenium](https://www.seleniumhq.org)

### Author

[James Bos](https://www.jamesbos.com)

## License

Licensed under the GPLv2 Licence - See a copy of the licence [here](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
