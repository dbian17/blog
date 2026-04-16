# blog

Welcome to my personal mind dump :)

## Testing

### Local Host
```
cd ~/blog/src/webapp
source /home/david/venv/bin/activate
flask --app ./api/controller.py run --debug
```

### Vercel Test
```
cd ~/blog/src/webapp
vercel deploy
```

## Deployment

Pushing to mainline will automatically deploy to prod

OR

```
cd ~/blog/src/webapp
vercel --prod
```

