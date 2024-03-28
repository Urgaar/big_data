from mrjob.job import MRJob

class TagCountPerMovie(MRJob):

    def mapper(self, _, line):
        try:
            userID, movieID, tag, timestamp = line.split(',')
            yield movieID, 1
        except ValueError:
            pass

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    TagCountPerMovie.run()
