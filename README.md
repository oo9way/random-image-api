
# Random Image Generator API

### [random-image.up.railway.app](https://radom-image.up.railway.app/) 
The Random Image Generator API is a versatile and user-friendly service that allows developers to access a vast collection of images for various use cases. Whether you need random images for testing, placeholders, or specific images with custom sizes for your application, this API has you covered.


## API Reference

#### Get random picture

```http
  GET /api/photo/
```


#### Get random picture with given size

```http
  GET /api/photo/?width=200&height=200
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `width`      | `integer` | **Required**. Width of image |
| `height`      | `integer` | **Required**. Height of image |


